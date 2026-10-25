# Procurement guidance

## Source strategy

Use **McMaster-Carr**, **VEX Robotics**, **Grainger**, and reputable electronics suppliers for durable, reusable mechanism components; use Amazon only when the ASIN, configuration, and seller can be fixed in the BOM. For optical projects, **Thorlabs**, **MKS/Newport**, and **B&H Photo Video** are permitted vendors when the BOM records the exact manufacturer item, optical specification, thread/interface, package yield, quantity, and direct link. A category link is useful for research, but it is **not a valid BOM entry**. An approved build must instead specify a manufacturer/supplier item number (or an Amazon ASIN), configuration, package yield, quantity, and direct product link. A vendor substitution is not approved merely because its nominal focal length or diameter appears similar; verify the complete mechanical and optical interface in a first article. The current item-level references and release gate are in [BUILD_STANDARD.md](BUILD_STANDARD.md).

For gears, all gears that mesh must have the same **type, pressure angle, and pitch/module**. McMaster's selection guide explains these compatibility conditions and the relation between tooth-count ratio, speed, and torque: [How to Choose a Gear](https://www.mcmaster.com/info/how-to-choose-a-gear.html).

## Reusable common kit — per table of 4–6 students

| Item | Functional specification | Qty. | McMaster-Carr | Amazon search |
| --- | --- | ---: | --- | --- |
| Fastener organizer | Machine screws, washers, and locknuts; #6-32 or M3/M4 family | 1 | [screws and bolts](https://www.mcmaster.com/products/screws/) | [machine-screw assortment](https://www.amazon.com/s?k=machine+screw+assortment+washers+nuts) |
| Shaft system | Choose one standard: 1/4 in or 5 mm shafts, collars, and matching bushings | 1 set | [shafts, collars, and bushings](https://www.mcmaster.com/products/power-transmission/) | [5 mm shaft kit](https://www.amazon.com/s?k=5mm+shaft+collar+bushing+kit) |
| Frame stock | **Not permitted in a released no-fabrication build.** Use a fixed-length, part-numbered rail, panel, enclosure, or molded component with factory mounting features. | — | [release rule](BUILD_STANDARD.md) | — |
| Tool set | Ruler, marker, supplied screwdriver/wrench/hex keys only | 1 set | [hand tools](https://www.mcmaster.com/products/hand-tools/) | [student tool set](https://www.amazon.com/s?k=small+student+hand+tool+set) |
| Consumables | Masking tape, string, rubber bands, zip ties, glue dots | 1 set | [cable ties](https://www.mcmaster.com/products/cable-ties/) | [STEM craft supplies](https://www.amazon.com/s?k=stem+craft+supplies+rubber+bands+craft+sticks) |

## Compatibility rule

Select either an inch or metric hardware system for a project and label every bin accordingly. Do not assume that a shaft, collar, gear bore, bearing, and fastener from mixed systems will fit. Record the selected system and each supplier part number in the event-specific purchase record.

## Budget status

All cost expectations in this repository are **planning estimates only**, not quotes. A first pilot should price a single complete kit plus 10–20% spare consumables, then record the actual receipt cost and yields for the next release.
