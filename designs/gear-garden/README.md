# Gear Garden: hand-cranked kinetic sculpture

![Gear Garden diagram](../../assets/gear-garden.svg)

![Illustrative 3D concept render of Gear Garden](render-concept-v1.png)

*Illustrative 3D concept render. The purchasable version trades sculpted flowers and a custom clear cover for a fully factory-perforated VEX plate sandwich: the gears remain visible through the top-hole pattern but inaccessible from above.*

![Graphical no-fabrication assembly flow](../../assets/manuals/catalog-toy-assembly-flow.svg)

Students build a hand-cranked gear train and add non-load-bearing cable-tie “petals.” The core lesson is speed ratio and direction reversal, not decorative precision.

**Status:** procurement-complete rendered concept; **not yet classroom-release ready.** The BOM buys every proposed component, including the no-cut guard strategy. A physical first article must verify gear mesh, shaft capture, crank clearance, and guard effectiveness before public use. See the [build standard](../../docs/BUILD_STANDARD.md).

## What the purchasable version changes

| Rendered feature | No-fabrication implementation |
| --- | --- |
| Individually mounted, open decorative gears | VEX acetal gears captured between two perforated aluminum plates |
| Clear shaped guard | Second perforated plate plus standoffs; its factory holes allow viewing but exclude fingers from the gear faces |
| Flower-shaped ornaments | Removable full-length cable ties, kept outside the plate sandwich and clear of teeth |
| Custom crank | 60-tooth gear and factory-hole 1x25 bar used as a large hand crank |

## Complete bill of materials — one Gear Garden

| Function | Exact item and purchased configuration | Buy | Use | Direct item link |
| --- | --- | ---: | ---: | --- |
| Perforated base and fixed upper finger guard | VEX V5 `276-2311`, 5 x 25 Aluminum Plate | 1 pack | 2 plates | [276-2311](https://www.vexrobotics.com/276-2311.html) |
| Shafts, flat bearings, shaft collars, standoffs, washers, #8-32 screws and nuts; one factory-hole 1x25 crank bar | VEX V5 `276-2161`, Metal & Hardware Kit | 1 kit | 4 shafts; 8 flat bearings; 8 standoffs; 1 bar; hardware as supplied | [276-2161](https://www.vexrobotics.com/276-2161.html) |
| Matched 24-DP gears | VEX V5 `276-2169`, Gear Kit | 1 kit | 1 each of 12T, 36T, 60T, and 84T gear | [276-2169](https://www.vexrobotics.com/gears.html) |
| Decorations and non-load-bearing labels | VEX V5 `276-1032`, cable ties | 1 pack | 8 ties | [276-1032](https://www.vexrobotics.com/276-1032.html) |
| Shared assembly tools | VEX V5 `276-1382`, Tool Kit | 1 shared kit | 1 wrench and 2 hex keys | [276-1382](https://www.vexrobotics.com/276-1382.html) |

No raw sheet, stock shaft, fabricated spacer, custom guard, or extra fastener is required.

## Item-specific assembly sequence

1. Place two `276-2311` plates parallel, with the first as the base and the second as the upper guard. Join them with eight supplied 1-in. VEX standoffs at the factory-hole grid, producing a protected internal gear space.
2. Install four VEX flat bearings in selected factory holes of both plates. Pass the supplied shafts through matched bearing pairs; capture each with supplied shaft collars so no shaft can drift into a plate.
3. Place the 12T, 36T, 60T, and 84T gears from `276-2169` between the plates. Begin with 12T-to-36T and 36T-to-60T meshes; use the 84T gear only after the first two meshes rotate freely. The teeth must mesh without forced contact.
4. Lock each driven gear to its shaft with a supplied collar or the gear’s intended shaft engagement. Bolt one `276-2161` 1x25 bar to the 60T gear’s factory mounting holes to make the hand crank. Its unused full length is intentional; do not shorten it.
5. Add up to eight full cable ties as petals/flags only on exterior hardware. Keep every tie end outside the sandwich and at least one gear radius from a mesh; do not trim the tails.
6. Turn the crank slowly through 20 revolutions. If any mesh binds, stop and reposition the shaft using only factory holes before allowing students to operate it.

## First-article checks before release

- Verify the selected gear centers give clearance/backlash rather than tooth-bottom contact; all gears in `276-2169` share the specified 24-DP, 20-degree system.
- Confirm the upper plate and standoff spacing prevent a child’s finger from reaching the faces or teeth while the crank is turned.
- Confirm the bar crank clears the plate, tabletop, nearby students, and its own cable-tie ornaments through a full rotation.

## Physics prompt

For two meshing external gears, \(\omega_2/\omega_1=-N_1/N_2\). The minus sign denotes direction reversal. Have students predict the direction and relative speed of the 36T and 60T gears before turning the crank, then compare prediction with observation.
