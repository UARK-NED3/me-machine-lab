# Design audit — 2026-10-25

## Scope and evidence status

This is a documentation and interface audit of the repository designs at commit time. It checks the stated BOMs, instructions, render-to-BOM correspondence, component-family interfaces, dimensions that can be bounded from catalog data, and prohibited operations in the [no-fabrication build standard](BUILD_STANDARD.md). It is **not** a physical first-article validation. Vendor availability, current pricing, fit between different manufacturers, motion quality, and safety remain unmeasured unless a project reports an actual pilot.

## Findings and disposition

| Design | Render status | Audit result | Concrete finding / required action |
| --- | --- | --- | --- |
| HydroGrab | Render added | **Blocked — legacy concept** | The BOM uses generic syringes/tubing/adapters, craft sticks or plywood, a cut/selected base, unspecified fasteners, tape, and facilitator hole punching/hot glue. It violates the exact-item and no-fabrication requirements; the catalog-parts render is a redesign target, not the listed build. Replace the BOM and instructions before procurement. |
| Rescue Hoist | Render added | **Blocked — legacy concept** | The BOM requires cutting shafts, drilling side plates, plywood, a selected spool, a selected guard, generic gears, and a wood handle. It violates the no-fabrication standard. It also lists four 24T and two 48T gears, while the written two-stage 24T-to-48T train uses only two 24T and two 48T gears. The catalog-parts render is a redesign target, not the listed build. |
| Crank Critter | Render added | **Blocked — legacy concept** | Craft sticks/plywood, dowels, cardboard, a punched crank disk, and generic hardware do not meet the exact-item/no-fabrication gate. The catalogue-parts render is a redesign target, not the listed build. Replace the BOM and instructions before procurement. |
| Cable-Car Dash | Render already present | **Corrected, still requires pilot** | The previous two-kit BOM could not cover the worst-case full-height drive-line path with a single 4-ft rope. The BOM now orders three `276-1546` kits: one uncut guide rope and two uncut ropes tied for the drive line. The enclosure-hole pattern, trolley retention, knots, and counterweight containment remain first-article checks. |
| Gear Garden | Render already present | **Interfaces consistent, pilot required** | `276-2169` supplies the stated 24-DP, 20° gear family, while `276-2161` supplies VEX square shafts, collars, bearings, #8-32 hardware, and four 1x25 bars. The gear centers and the perforated-plate finger barrier must still be physically verified. |
| Pinball Lab | Render already present | **Interfaces partly unverified** | VEX shafts and `228-3510` rubber collars share the specified 0.125-in. square shaft interface. The McMaster spring-hinge and spring-plunger mounting-hole patterns have not been physically checked against the VEX 0.5-in. grid; the BOM must remain a rendered concept until that pilot is performed. |
| Springy Wobblebot | Render already present | **Exact-source replacement identified; retention risk remains** | The discontinued/small-vendor electrical items are replaced by an exact direct-distributor set: Vybronics `VZ4TL2B0370055L` motor, Keystone `2490SW` switched 2xAA holder, and Adafruit `4100` insulated test leads through DigiKey, plus exact Panasonic eneloop battery/charger ASINs. The motor series' 2.2–3.6 V operating range bounds a two-cell NiMH supply (2.4 V nominal). The McMaster spring assortment still requires selection of one compartment, and motor/spring/bumper retention needs a physical pilot before release. |
| Build-a-Monocular Lab | Render already present | **Corrected, still requires optical pilot** | The prior `SM1L10 + SM1L30 + SM1V05` mechanical stack was longer than the 100 mm paraxial target before allowing for lens mounting offsets. It is corrected to `SM1L10 + SM1L20 + SM1V05` (88.9 mm nominal tube length before offsets) with fine focus for first-article tuning. All interfaces are SM1 / Ø1 in, but actual infinity focus, lens retention, and measured magnification remain unverified. |

## Cross-project fastener and fabrication review

- The catalog VEX designs share the `276-2161` #8-32 hardware family, VEX 0.125-in. square shafts, matching bearings/collars, and the `276-1382` hex-tool family. No mixed metric/inch fastener system is specified within those designs.
- The catalog designs use factory-perforated VEX parts and uncut rope/cable ties. The documented allowed operations are hand fastening, threading, tying, and applying supplied adhesive bumpers.
- HydroGrab, Rescue Hoist, and Crank Critter still violate the standard as written. Their rows are retained in the consolidated purchase workbook as **blocked source records**, not orderable parts, so the purchase list does not disguise the missing item numbers or prohibited operations.
- A visual render is not evidence of physical compatibility. All designs remain below the repository release gate until a physical first article has checked fit, movement, containment, and safety.

## Current manufacturer evidence used in the audit

- VEX reports that `276-2161` supplies four 1x25 steel bars, VEX shafts/bearings/collars, and #8-32 fasteners; its current catalog also lists the package contents for the `276-2169` gear kit. [VEX Metal & Hardware Kit](https://www.vexrobotics.com/276-2161.html), [VEX Gear Kit](https://www.vexrobotics.com/gears.html)
- VEX lists `276-1546` with one 4-ft rope per kit, which supports the Cable-Car Dash length correction. [VEX Winch & Pulley Kit](https://www.vexrobotics.com/276-1546.html)
- VEX lists `228-3510` as compatible with VEX 0.125-in. square shafts. [VEX Rubber Shaft Collar](https://www.vexrobotics.com/228-3510.html)
- Thorlabs lists SM1 lens-tube lengths and the adjustable tube interface used in the monocular correction. [Thorlabs SM1 lens tubes](https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=3307), [Thorlabs adjustable lens tubes](https://www.thorlabs.com/catalogpages/210.pdf)
- DigiKey currently lists the exact Vybronics motor and Keystone switched battery holder used in the revised Wobblebot BOM. [Vybronics VZ4TL2B0370055L](https://www.digikey.com/en/products/detail/vybronics-inc/VZ4TL2B0370055L/15220806), [Keystone 2490SW](https://www.digikey.com/en/products/detail/keystone-electronics/2490SW/12751690)
- The corrected 3M page identifies the `SJ5012BL` bumper mini-pack; its current distributor price is not asserted in the workbook. [3M SJ5012 Bumpon](https://www.3m.com/3M/en_US/p/d/v000057350/)
