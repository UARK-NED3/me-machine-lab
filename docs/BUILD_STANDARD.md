# No-Fabrication Build Standard

This repository uses **no-fabrication** in a literal sense. A student or facilitator must be able to complete a released build by selecting, positioning, and fastening purchased parts. They must not alter the purchased part.

## Allowed operations

- Tighten or loosen a supplied screw, nut, T-slot fastener, shaft collar, or set screw with a hand tool.
- Route or tie a supplied, uncut cord; attach a cable tie; place a ball; adjust a spring only within its supplied configuration; apply a removable label; or press on a supplied adhesive bumper.
- Use a threaded hole, clearance hole, slot, T-slot, bearing bore, or mounting pattern that already exists on the purchased part.

## Prohibited operations

- Cut, drill, punch, mill, turn, grind, file, saw, bend, heat-form, weld, solder, or 3D-print a build component.
- Use a raw-material length, sheet, rod, or panel that implies a user-selected cut length.
- Substitute a generic purchasing category for a part number.

## Release gate

A design is **build-ready** only when its BOM has an exact supplier item number (or Amazon ASIN), quantity, package/yield, and direct item link for every purchased item; its instructions use only the allowed operations; and a physical pilot has checked fit, motion, containment, and safety. Until then it is a **rendered concept**. A render or SVG is an explanatory visual, not evidence that an assembly has been physically validated.

## Complete-BOM convention

The four catalog-toy projects now use a procurement-complete, lower-fidelity route based chiefly on VEX V5 fixed-size, perforated components. This is intentional: it replaces the custom-looking rails, guards, and shaped bodies in the renders with factory-hole metal and plastic components that students can assemble without fabrication. A BOM row that says **kit** is a single, exact purchasing line; its ``use`` column states how many of the included pieces the project consumes. The kit contents must not be silently substituted.

The BOMs are complete for purchasing, not yet pilot-certified for fit or classroom use. In particular, the proposed alignment of the McMaster hinge/plunger to the VEX hole pattern, counterweight travel, exposed-mesh guarding, adhesive-foot retention, and all moving clearances must be checked on a physical first article.

## Current catalog references verified at item level

| Supplier item | Purchased configuration | Permitted role | Direct item link |
| --- | --- | --- | --- |
| McMaster `5537T2` | 20 mm T-slotted rail, 6 in. length | Pre-cut cross member or perimeter member | [5537T2](https://www.mcmaster.com/5537T2/) |
| McMaster `5537T368` | 20 mm T-slotted rail, 12 in. length | Pre-cut base rail or tower member | [5537T368](https://www.mcmaster.com/5537T368/) |
| McMaster `8478A1` | Nonlocking, plate-mount retractable spring plunger; zinc-alloy plate and steel nose | Manual launcher only; mount through its factory holes | [8478A1](https://www.mcmaster.com/8478A1/) |
| McMaster `9645K2` | 92-piece, 29-size compression/extension spring assortment | Prototype return springs only after a pilot selects a specific included spring | [9645K2](https://www.mcmaster.com/9645K2/) |
| McMaster `2664N316` | Module 0.5, 24-tooth, 20 degree pressure-angle steel spur gear; 5 mm set-screw bore | Gear Garden drive gear | [2664N316](https://www.mcmaster.com/2664N316/) |
| McMaster `2664N321` | Module 0.5, 36-tooth, 20 degree pressure-angle steel spur gear; 5 mm set-screw bore | Gear Garden driven gear | [2664N321](https://www.mcmaster.com/2664N321/) |
| McMaster `3684N12` | 2MGT, 20-tooth, 5 mm finished-bore timing pulley with set screw | Cable-Car Dash cable-drive prototype | [3684N12](https://www.mcmaster.com/3684N12/) |

The items above are source-checked against McMaster’s catalog as of the repository revision date. They are not a completed, pilot-validated kit. In particular, a released version still needs exact factory-featured mounting hardware, pre-made car/body components, and a confirmed safety envelope. Do not treat a category-page link as a substitute for that work.
