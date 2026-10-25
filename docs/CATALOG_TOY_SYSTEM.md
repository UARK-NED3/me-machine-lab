# Catalog-parts toy system

This track treats industrial catalog parts as a toy-construction system. The aim is not to imitate a consumer kit; it is to let students combine recognizable engineering elements into playful machines without wood shaping, laser cutting, or custom machining.

## Shared interface standard

For a first pilot, use the following system consistently:

| Interface | Recommended choice | Why it matters |
| --- | --- | --- |
| Structure | VEX V5 factory-perforated plates, C-channels, rails, and gussets | Fixed-size factory-hole parts create frames without student cutting. |
| Rotary components | VEX 0.125-in. square shaft, VEX bearing, and VEX shaft collar | One shaft family prevents most fit errors in the mechanical builds. |
| Gears | VEX `276-2169` 24-DP, 20° pressure-angle gear family | The entire Gear Garden drive train uses one specified compatible family. |
| Fasteners | VEX `276-2161` supplied #8-32 screw/nut/washer family | One supplied tool/hardware system streamlines assembly. |
| Decorative/function pieces | Colored cable ties, plastic knobs, small boxes, springs, wheels, and caps | These are real catalog components—not custom silhouettes—and give each toy identity. |

VEX lists the current C-channel, plate, gusset, gear, and hardware kits used by the four BOMs. [VEX structure](https://www.vexrobotics.com/v5-structure.html) Gear pairs must share type, pressure angle, and pitch/module; use one compatible family throughout a model. [Gear selection guide](https://www.mcmaster.com/info/how-to-choose-a-gear.html) The system description is not a purchase list: the project-level exact-item BOM and [no-fabrication release gate](BUILD_STANDARD.md) control what may enter a released design.

## Why this is better suited to the outreach goal

- Students see the components found in real machines: bearings, shafts, collars, pulleys, gears, springs, and brackets.
- A successful toy remains disassemblable and becomes the component pool for a different toy next time.
- Failures are legible: a slipping collar, unmeshed gear, misaligned pulley, weak spring, or poorly balanced rotor each has a mechanical cause.

## Project menu

| Project | Play pattern | Core parts | Main transfer task |
| --- | --- | --- | --- |
| Pinball Lab | Score and redesign a tabletop game | Perforated plate, springs, bumpers, ball | Tune the game for longest play or highest score |
| Cable-Car Dash | Move cargo between towers | Pulleys, cord, counterweight, rails | Deliver a payload accurately without overshoot |
| Gear Garden | Make a hand-cranked moving sculpture | Plastic gears, shafts, collars, bearings | Create a repeating motion that is visually intentional |
| Springy Wobblebot | Make a silly vibrating creature | Motor, eccentric collar, springs, enclosure | Travel farthest in 10 s without toppling |

## Procurement status

The four project READMEs now contain **procurement-complete, exact-item BOMs** with package yield and direct item links. They deliberately use VEX fixed-size perforated structure as a lower-fidelity alternative to the custom-looking render hardware. The remaining release condition is physical—not clerical: fit, motion, containment, guarding, electrical integrity, availability, and safety still require first-article pilot verification before a configuration is offered to students.
