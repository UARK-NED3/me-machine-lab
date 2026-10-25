# Pinball Lab: reconfigurable tabletop game

![Pinball Lab diagram](../../assets/pinball-lab.svg)

![Illustrative 3D concept render of Pinball Lab](render-concept-v1.png)

*Illustrative 3D concept render, not a dimensioned CAD assembly or a substitute for the exact-item BOM and physical pilot.*

![No-fabrication graphical assembly method](../../assets/manuals/catalog-toy-assembly-flow.svg)

Build a small hand-powered pinball game from a perforated panel, ordinary brackets, fasteners, springs, and bumpers. Teams earn points by defining their own scoring zones, then change one feature to control energy loss and ball paths.

**Design status:** rendered concept; **not** yet an approved student build. The earlier category-only BOM has been retired. A full exact-item, no-fabrication BOM and physical pilot are required by the [build standard](../../docs/BUILD_STANDARD.md). This project intentionally excludes wood, custom-shaped plates, and any cutting or machining.

## Exact purchased components captured to date — not a complete BOM

| Function | Exact supplier item | Qty. | Direct item link |
| --- | --- | ---: | --- |
| Fixed-length frame member | McMaster `5537T368`, 20 mm T-slotted rail, 12 in. | 2 | [5537T368](https://www.mcmaster.com/5537T368/) |
| Fixed-length cross member | McMaster `5537T2`, 20 mm T-slotted rail, 6 in. | 2 | [5537T2](https://www.mcmaster.com/5537T2/) |
| Play ball | McMaster `9613K21`, 3/8 in. off-white nylon ball, 100-pack | 1 | [9613K21](https://www.mcmaster.com/9613K21/) |
| Manual launcher candidate | McMaster `8478A1`, nonlocking plate-mount retractable spring plunger | 1 | [8478A1](https://www.mcmaster.com/8478A1/) |
| Prototype spring pool | McMaster `9645K2`, 92-piece compression/extension spring assortment | 1 kit | [9645K2](https://www.mcmaster.com/9645K2/) |

**Release blockers:** a pre-made play surface, factory-featured bumper mounts, flipper modules, and every joining fastener have not yet been selected at item-number level. Do not purchase or improvise these items from a category page.

## Conceptual assembly sequence — replace with an item-specific graphical manual after the release gate

1. Bolt four rails or angle brackets around the playfield to make a raised perimeter; leave a release gap at the lower right.
2. Mount the launcher at the lower end. It must launch only toward the raised boundary, not out of the table.
3. Add rubber bumpers through existing holes, beginning with a symmetric pattern. Mount scoring labels beside them.
4. Build two pivoting flippers from small angle brackets and fasteners. Add light return springs. Verify each flipper moves freely and returns without trapping the ball.
5. Add two spring kickers: a washer-on-bolt lever that is struck by the ball, with a small return spring, is sufficient.
6. Test one ball at a time with a soft catcher at the lower opening. Change one feature—bumper spacing, spring preload, playfield slope, or flipper location—between trials.

## Physics prompt

The ball’s kinetic energy changes through impacts, rolling resistance, sliding friction, and spring work. A bumper does not create energy; it redirects the ball and, if spring-loaded, returns some stored elastic energy. Compare the number of bumper contacts and play time before and after one design change.

## Success criteria

- The ball remains inside the perimeter during normal play.
- A student can reconfigure at least three bumpers using only a screwdriver.
- Teams can explain one observed tradeoff between scoring difficulty and game duration.
