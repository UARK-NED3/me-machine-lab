"""Build the rendered-concept assembly-manual PDF from the canonical design READMEs.

The generated manual is intentionally explicit about the repository release gate:
these are detailed first-article build procedures, not classroom-release evidence.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    KeepTogether,
    LongTable,
    PageBreak,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.graphics.shapes import Circle, Drawing, String
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "ME_Hands_On_Project_Detailed_Assembly_Manuals.pdf"
TEMP_DIAGRAM_DIR = ROOT / "tmp" / "pdfs"
INKSCAPE = Path("C:/Program Files/Inkscape/bin/inkscape.exe")

PROJECTS = [
    {
        "slug": "cable-car-dash",
        "name": "Cable-Car Dash",
        "audience": "Grades 6-12 | 60-90 min",
        "goal": "Build a counterweighted gondola, then tune payload and stopping error.",
        "render": "render-concept-v1.png",
        "boundary": "Hand power only. Keep the counterweight inside the tower-base footprint. Start with no more than a 50 g gondola payload until the first article passes its checks.",
        "preflight": [
            "Choose a level tabletop away from its edge. Mark the counterweight travel envelope and keep hands out of it.",
            "Separate the guide rope from the drive rope before building. Do not cut, melt, splice, or substitute rope.",
            "Confirm that each pulley, shaft collar, and tower fastener is present before raising either tower.",
        ],
    },
    {
        "slug": "crank-critter",
        "name": "Crank Critter",
        "audience": "Grades 5-10 | 45-75 min",
        "goal": "Build a stationary two-cam automaton and investigate timing, follower stroke, and gear reduction.",
        "render": "render-bom-constrained-v2.png",
        "boundary": "Hand crank only. This is a stationary automaton, not a walking machine. Stop before adjusting a cam, follower, gear, or pivot.",
        "preflight": [
            "Sort the frame hardware, bearings, collars, shafts, 12T gear, 36T gear, cams, followers, and hand crank into separate groups.",
            "Use the VEX 24-DP gear pair only; do not combine gears from different pitch systems.",
            "Keep the frame on a flat table. The base must sit without rocking before a crank is installed.",
        ],
    },
    {
        "slug": "gear-garden",
        "name": "Gear Garden",
        "audience": "Grades 5-12 | 45-75 min",
        "goal": "Make a guarded hand-cranked gear sculpture and predict speed and direction changes.",
        "render": "render-concept-v1.png",
        "boundary": "Turn only by the prescribed hand crank. The upper plate is a finger barrier, not decoration; do not operate if any student can reach a gear mesh.",
        "preflight": [
            "Pull exactly two perforated plates and eight matching standoffs; do not replace them with cut sheet or improvised spacers.",
            "Lay out the 12T, 36T, 60T, and 84T gears. Confirm each has the VEX square-shaft interface before assembly.",
            "Keep cable ties outside the plate sandwich and untrimmed. They are visual indicators only, never load-bearing members.",
        ],
    },
    {
        "slug": "hydrograb",
        "name": "HydroGrab",
        "audience": "Grades 6-10 | 75-90 min",
        "goal": "Build a water-actuated arm and compare predicted with observed force and displacement.",
        "render": "render-bom-constrained-v2.png",
        "boundary": "Use water, needleless syringes, and lightweight dry objects only. Apply hand force only. Keep all water away from electrical equipment and wipe spills immediately.",
        "preflight": [
            "Count six identical 20 mL needleless syringes. Pair them before filling so each master and slave has the same nominal bore.",
            "Inspect the Luer ends on each received extension set. Do not force a connection; use the listed female-to-female adapter only when its connector gender is required.",
            "Arrange a tray, towels, and a dry landing area before filling any circuit.",
        ],
    },
    {
        "slug": "monocular-lab",
        "name": "Build-a-Monocular Lab",
        "audience": "Grades 8-12 | 45-60 min",
        "goal": "Assemble a 3x Galilean monocular and test focus and angular magnification using distant terrestrial targets.",
        "render": "render-concept-v1.png",
        "boundary": "Terrestrial viewing only. Never point the instrument at the Sun, a laser, welding arc, or bright specular reflection. Handle every optic by its edge.",
        "preflight": [
            "Use a clean, dry, well-lit table. Remove food, liquids, loose hardware, and abrasive materials from the work area.",
            "Verify the objective is mounted and the negative eyepiece is free of chips, cracks, fingerprints, and damaged coatings before threading parts together.",
            "Identify the rotating focus section and its locking ring before installing the eyepiece. Do not use pliers, tape, adhesive, or a cut spacer.",
        ],
    },
    {
        "slug": "pinball-lab",
        "name": "Pinball Lab",
        "audience": "Grades 6-12 | 60-90 min",
        "goal": "Build a reconfigurable tabletop pinball game and quantify how layout changes affect ball paths and game time.",
        "render": "render-concept-v1.png",
        "boundary": "Use one 3/8 in nylon ball per table. Do not release the launcher toward a person. Keep fingers clear of spring hinges while another person launches the ball.",
        "preflight": [
            "Place all perforated plates with their factory hole rows parallel. Confirm the long rails and both end barriers are present before adding the ball.",
            "Select four straight, undamaged VEX shafts and eight rubber collars for the post bumpers.",
            "Keep the plunger uncompressed until the launcher adapter is fully bolted and its travel is enclosed by the perimeter rails.",
        ],
    },
    {
        "slug": "rescue-hoist",
        "name": "Rescue Hoist",
        "audience": "Grades 7-12 | 90-120 min",
        "goal": "Build a two-stage 9:1 hand winch and compare torque reduction with input-turn count.",
        "render": "render-bom-constrained-v2.png",
        "boundary": "Hand operation only. Use the specified 100 g hanging test weight and a 20 cm lift above a clear, padded landing surface. Never lift over a person or bypass the ratchet.",
        "preflight": [
            "Mark a no-hand zone below the hanging test weight and around the gear meshes before any rope is installed.",
            "Set aside two 12T and two 36T gears from the same VEX kit. Do not substitute a 4:1 stage; the intended train is 3:1 times 3:1.",
            "Inspect the stock rope, drum, pawl, and ratchet. Stop if the rope is frayed or the pawl does not move freely.",
        ],
    },
    {
        "slug": "springy-wobblebot",
        "name": "Springy Wobblebot",
        "audience": "Grades 5-10 | 30-60 min",
        "goal": "Build a low-voltage vibrating creature and investigate how unbalance, compliant legs, and friction produce motion.",
        "render": "render-bom-faithful-v2.png",
        "boundary": "Use only the listed two-cell AA NiMH supply. Turn power off before any adjustment. Do not use wall power, USB power, alkaline cells, or damaged battery cells.",
        "preflight": [
            "Set the battery holder switch to OFF. Install the two charged cells but do not connect the clip leads yet.",
            "Choose four identical springs and inspect them for sharp ends, permanent bends, or damage.",
            "Prepare a clear floor tray for motion tests. Keep hands, hair, clothing, and loose objects outside the eccentric-mass sweep.",
        ],
    },
]


def clean_markdown(value: str) -> str:
    """Convert the compact README text into readable PDF prose."""
    def plain_latex(match: re.Match[str]) -> str:
        expression = match.group(1)
        replacements = {
            r"\\mathrm{cw}": "cw",
            r"\\mathrm{car}": "car",
            r"\\mathrm{payload}": "payload",
            r"\\omega": "omega",
            r"\\theta": "theta",
            r"\\approx": "approximately",
            r"\\times": "x",
        }
        for source, replacement in replacements.items():
            expression = expression.replace(source, replacement)
        expression = expression.replace("{", "").replace("}", "").replace("\\", "")
        return expression

    value = re.sub(r"\\\((.*?)\\\)", plain_latex, value)
    value = re.sub(r"!\[[^]]*\]\([^)]*\)", "", value)
    value = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r"\1", value)
    value = value.replace("**", "").replace("`", "")
    value = value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"\s+", " ", value).strip()


def diagram_file(project: dict) -> Path | None:
    """Rasterize the repository's own SVG diagram for reliable PDF embedding.

    The diagrams are existing project assets rather than generated artwork, so the
    visible mechanism labels remain traceable to the design documentation.
    """
    source = ROOT / "assets" / f"{project['slug']}.svg"
    if project["slug"] == "monocular-lab":
        source = ROOT / "assets" / "manuals" / "monocular-lab-assembly.svg"
    if not source.exists() or not INKSCAPE.exists():
        return None
    TEMP_DIAGRAM_DIR.mkdir(parents=True, exist_ok=True)
    target = TEMP_DIAGRAM_DIR / f"{project['slug']}-diagram.png"
    subprocess.run(
        [str(INKSCAPE), str(source), "--export-type=png", f"--export-filename={target}", "--export-width=1500"],
        check=True,
        capture_output=True,
        text=True,
    )
    return target if target.exists() else None


def sentence_groups(step: str) -> list[str]:
    """Keep each student-facing action card short enough to scan while building."""
    parts = [part.strip() for part in re.split(r"(?<=[.!?])\s+|;\s+", step) if part.strip()]
    if not parts:
        return [step]
    groups: list[str] = []
    current: list[str] = []
    for part in parts:
        current.append(part)
        if len(" ".join(current)) > 175 or len(current) == 2:
            groups.append(" ".join(current))
            current = []
    if current:
        groups.append(" ".join(current))
    return groups


def section(lines: list[str], heading_match: str) -> list[str]:
    start = next((i for i, line in enumerate(lines) if line.lower().startswith("##") and heading_match in line.lower()), None)
    if start is None:
        return []
    result: list[str] = []
    for line in lines[start + 1 :]:
        if line.startswith("## "):
            break
        result.append(line.rstrip())
    return result


def first_paragraph(lines: list[str], heading_match: str) -> str:
    for line in section(lines, heading_match):
        if line and not line.startswith("|") and not line.startswith("*") and not line.startswith("**"):
            return clean_markdown(line)
    return ""


def parse_table(lines: list[str]) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines:
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [clean_markdown(cell) for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r"[-: ]+", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def numbered_steps(lines: list[str]) -> list[str]:
    steps: list[str] = []
    buffer: list[str] = []
    for line in lines:
        match = re.match(r"^\d+\.\s+(.*)", line)
        if match:
            if buffer:
                steps.append(clean_markdown(" ".join(buffer)))
            buffer = [match.group(1)]
        elif buffer and line and not line.startswith("|"):
            buffer.append(line)
    if buffer:
        steps.append(clean_markdown(" ".join(buffer)))
    return steps


def bullets(lines: list[str]) -> list[str]:
    return [clean_markdown(line[2:]) for line in lines if line.startswith("- ")]


def make_styles():
    styles = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("ManualTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=colors.HexColor("#123B5D"), alignment=TA_CENTER, spaceAfter=10),
        "subtitle": ParagraphStyle("ManualSubtitle", parent=styles["BodyText"], fontName="Helvetica", fontSize=10, leading=14, textColor=colors.HexColor("#455A64"), alignment=TA_CENTER, spaceAfter=12),
        "h1": ParagraphStyle("ManualH1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=colors.HexColor("#123B5D"), spaceBefore=12, spaceAfter=6),
        "h2": ParagraphStyle("ManualH2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=colors.HexColor("#1E5A88"), spaceBefore=10, spaceAfter=4),
        "body": ParagraphStyle("ManualBody", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.2, leading=12.4, spaceAfter=5),
        "small": ParagraphStyle("ManualSmall", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.5, leading=9.2, spaceAfter=2),
        "step": ParagraphStyle("ManualStep", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.4, leading=13.0, leftIndent=0, spaceAfter=7),
        "stepdo": ParagraphStyle("ManualStepDo", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=10.2, leading=13.4, textColor=colors.HexColor("#123B5D"), spaceAfter=4),
        "stepcheck": ParagraphStyle("ManualStepCheck", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.5, leading=10.4, textColor=colors.HexColor("#36515E"), spaceAfter=2),
        "stepstop": ParagraphStyle("ManualStepStop", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=8.5, leading=10.4, textColor=colors.HexColor("#9A3C12"), spaceAfter=2),
        "callout": ParagraphStyle("ManualCallout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9.2, leading=12.2, textColor=colors.HexColor("#7A2E0E"), spaceAfter=5),
        "table": ParagraphStyle("ManualTable", parent=styles["BodyText"], fontName="Helvetica", fontSize=6.5, leading=7.8),
        "tablehead": ParagraphStyle("ManualTableHead", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=6.5, leading=7.8, textColor=colors.white),
    }


def footer(canv: canvas.Canvas, doc: SimpleDocTemplate) -> None:
    canv.saveState()
    page = canv.getPageNumber()
    canv.setStrokeColor(colors.HexColor("#D6E2EA"))
    canv.line(0.55 * inch, 0.48 * inch, 7.95 * inch, 0.48 * inch)
    canv.setFont("Helvetica", 7.5)
    canv.setFillColor(colors.HexColor("#546E7A"))
    canv.drawString(0.55 * inch, 0.33 * inch, "ME Machine Lab | Detailed Assembly Manuals | Rendered concepts: first article required")
    canv.drawRightString(7.95 * inch, 0.33 * inch, f"Page {page}")
    canv.restoreState()


def bullet_list(items: list[str], styles: dict) -> list:
    flow = []
    for item in items:
        flow.append(Paragraph(f"• {item}", styles["body"]))
    return flow


def number_badge(number: str) -> Drawing:
    """A large, print-friendly number that makes the next task unambiguous."""
    drawing = Drawing(0.64 * inch, 0.64 * inch)
    drawing.add(Circle(0.32 * inch, 0.32 * inch, 0.27 * inch, fillColor=colors.HexColor("#1E5A88"), strokeColor=colors.HexColor("#123B5D")))
    drawing.add(String(0.32 * inch, 0.245 * inch, number, fontName="Helvetica-Bold", fontSize=13, fillColor=colors.white, textAnchor="middle"))
    return drawing


def step_card(number: str, instruction: str, styles: dict) -> Table:
    """Create a visual Do-Check-Stop card suitable for a young builder with an adult."""
    content = [
        Paragraph(f"<b>DO:</b> {instruction}", styles["stepdo"]),
        Paragraph("<b>CHECK:</b> Gently move the part by hand. It should fit through an existing hole or thread and should not need force.", styles["stepcheck"]),
        Paragraph("<b>STOP AND ASK AN ADULT:</b> if a part binds, a fastener will not start, a rope/tube/wire rubs, or you think a part needs cutting or drilling.", styles["stepstop"]),
    ]
    table = Table([[number_badge(number), content]], colWidths=[0.78 * inch, 6.35 * inch], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F3F8FB")),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#B7D0DE")),
        ("LINEBEFORE", (1, 0), (1, -1), 0.5, colors.HexColor("#D7E4EB")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 4),
        ("RIGHTPADDING", (0, 0), (0, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (1, 0), (1, -1), 8),
        ("RIGHTPADDING", (1, 0), (1, -1), 7),
    ]))
    return table


def bom_table(rows: list[list[str]], styles: dict) -> LongTable:
    if not rows:
        return LongTable([[Paragraph("No BOM table was found in the source README.", styles["table"])]], colWidths=[7.25 * inch])
    header = rows[0]
    # Keep the manual readable: function, exact configuration, and quantity/use are the essential pull-list fields.
    selected = [0, 1, 2] if len(header) >= 3 else list(range(len(header)))
    data = [[Paragraph(header[i], styles["tablehead"]) for i in selected]]
    for row in rows[1:]:
        padded = row + [""] * (max(selected) + 1 - len(row))
        data.append([Paragraph(padded[i], styles["table"]) for i in selected])
    widths = [1.25 * inch, 4.75 * inch, 1.25 * inch] if len(selected) == 3 else [7.25 * inch / len(selected)] * len(selected)
    table = LongTable(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E5A88")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#C8D6DF")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F7FAFC")),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return table


def project_flow(project: dict, styles: dict) -> list:
    source = ROOT / "designs" / project["slug"] / "README.md"
    lines = source.read_text(encoding="utf-8").splitlines()
    title = clean_markdown(next(line[2:] for line in lines if line.startswith("# ")))
    purpose = first_paragraph(lines, "purpose")
    bom = parse_table(section(lines, "bill of materials"))
    assembly = numbered_steps(section(lines, "assembly sequence"))
    checks = bullets(section(lines, "first-article"))
    troubleshooting_rows = parse_table(section(lines, "troubleshooting"))
    physics = first_paragraph(lines, "physics prompt")
    mechanism_diagram = diagram_file(project)

    flow = [
        Paragraph(title, styles["title"]),
        Paragraph(project["audience"], styles["subtitle"]),
        Paragraph("DRAFT INSTRUCTION MANUAL - RENDERED CONCEPT; PHYSICAL FIRST ARTICLE REQUIRED BEFORE CLASSROOM USE", styles["callout"]),
        Paragraph(project["goal"], styles["body"]),
    ]
    image_path = source.parent / project["render"]
    if image_path.exists():
        img = Image(str(image_path))
        max_width, max_height = 6.8 * inch, 3.9 * inch
        ratio = min(max_width / img.imageWidth, max_height / img.imageHeight)
        img.drawWidth = img.imageWidth * ratio
        img.drawHeight = img.imageHeight * ratio
        flow += [Spacer(1, 3), img, Spacer(1, 5)]
    flow += [
        Paragraph("1. Purpose and status", styles["h1"]),
        Paragraph(purpose, styles["body"]),
        Paragraph("This manual describes an exact-catalog, no-fabrication build sequence. The accompanying render communicates intended arrangement only; it does not verify dimensions, fit, strength, containment, or classroom safety.", styles["body"]),
        Paragraph("2. Safety boundary", styles["h1"]),
        Paragraph(project["boundary"], styles["callout"]),
        Paragraph("Use only factory-provided holes, threads, bores, mounting patterns, and supplied fasteners. Do not cut, drill, punch, mill, saw, bend, heat-form, solder, glue, or 3D-print any component.", styles["body"]),
    ]
    if mechanism_diagram:
        diagram = Image(str(mechanism_diagram))
        max_width, max_height = 6.8 * inch, 3.0 * inch
        ratio = min(max_width / diagram.imageWidth, max_height / diagram.imageHeight)
        diagram.drawWidth = diagram.imageWidth * ratio
        diagram.drawHeight = diagram.imageHeight * ratio
        flow += [KeepTogether([
            Paragraph("What you are making", styles["h2"]),
            Paragraph("Use this labeled picture to match the big parts before you begin. It explains the intended mechanism; it does not replace the numbered build cards below.", styles["small"]),
            diagram,
            Spacer(1, 6),
        ])]
    flow += [Paragraph("3. Before building: inventory and set up", styles["h1"])]
    flow += bullet_list(project["preflight"], styles)
    flow += [
        Paragraph("Pull-list bill of materials", styles["h2"]),
        Paragraph("Use the exact vendor item or ASIN shown below. The canonical README in the matching design folder retains the direct procurement hyperlinks and package-yield notes.", styles["small"]),
        bom_table(bom, styles),
        Spacer(1, 8),
        Paragraph("4. Step-by-step assembly", styles["h1"]),
        Paragraph("Complete the cards from top to bottom. The large blue circle tells you the next action. A child can read the card and do the action with an adult nearby; the orange STOP line tells everyone when to pause and ask for help.", styles["body"]),
    ]
    card_number = 1
    for step in assembly:
        for child_action in sentence_groups(step):
            flow += [step_card(str(card_number), child_action, styles), Spacer(1, 6)]
            card_number += 1
    flow += [
        Paragraph("5. First-article release checks", styles["h1"]),
        Paragraph("A build is not ready for student operation until a facilitator completes and records each applicable check below.", styles["body"]),
    ]
    flow += bullet_list(checks, styles)
    if troubleshooting_rows:
        flow += [Paragraph("6. Troubleshooting", styles["h1"]), bom_table(troubleshooting_rows, styles)]
    if physics:
        flow += [Paragraph("7. Engineering investigation", styles["h1"]), Paragraph(physics, styles["body"])]
    flow += [
        Paragraph("Closeout", styles["h2"]),
        Paragraph("Turn off or unload the mechanism, return reusable components to labeled containers, dry any water system, and record one configuration change plus one observed result. Remove any damaged, loose, frayed, leaking, or hot component from service.", styles["body"]),
        PageBreak(),
    ]
    return flow


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    styles = make_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.58 * inch,
        bottomMargin=0.62 * inch,
        title="ME Machine Lab Detailed Assembly Manuals",
        author="NED3 Laboratory",
    )
    flow = [
        Spacer(1, 0.6 * inch),
        Paragraph("ME Machine Lab", styles["title"]),
        Paragraph("Detailed Step-by-Step Assembly Manuals", styles["title"]),
        Paragraph("Eight catalog-parts STEM outreach projects", styles["subtitle"]),
        Spacer(1, 0.25 * inch),
        Paragraph("Important release status", styles["h1"]),
        Paragraph("Every project in this manual is a procurement-complete rendered concept. It is not yet a classroom-release design. A physical first article must verify all interfaces, motion, containment, and the project-specific safety boundary before students operate it.", styles["callout"]),
        Paragraph("No-fabrication rule", styles["h1"]),
        Paragraph("Students and facilitators may select, position, thread, fasten, tie, route, and adjust catalog parts through their existing features. They may not alter a purchased part. Cutting, drilling, machining, sanding, bending, heat-forming, welding, soldering, or 3D-printing a build component is outside this manual.", styles["body"]),
        Paragraph("How to use this manual", styles["h1"]),
        Paragraph("Read the project safety boundary first, inventory exact catalog parts, assemble in sequence, verify each step by hand, then complete the first-article release checks. The detailed product links and price information are maintained in the design README files and consolidated purchase list because vendor availability changes.", styles["body"]),
        Paragraph("Included projects", styles["h1"]),
    ]
    flow += bullet_list([f"{project['name']}: {project['goal']}" for project in PROJECTS], styles)
    flow += [Spacer(1, 12), Paragraph(f"Generated from repository design READMEs on {date(2026, 11, 4).isoformat()}.", styles["small"]), PageBreak()]
    for project in PROJECTS:
        flow += project_flow(project, styles)
    try:
        doc.build(flow, onFirstPage=footer, onLaterPages=footer)
    finally:
        if TEMP_DIAGRAM_DIR.exists():
            shutil.rmtree(TEMP_DIAGRAM_DIR)
        if TEMP_DIAGRAM_DIR.parent.exists() and not any(TEMP_DIAGRAM_DIR.parent.iterdir()):
            TEMP_DIAGRAM_DIR.parent.rmdir()
    print(OUTPUT)


if __name__ == "__main__":
    main()
