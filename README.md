# ME Machine Lab

Open, hands-on mechanical-engineering outreach projects for students who learn by designing, building, measuring, and improving real mechanisms.

> **Design status — proposed, not yet build-validated.** The first release provides facilitator-ready concepts, sourceable bills of materials, and assembly procedures. Dimensions, load limits, sourcing substitutions, and run time must be pilot-tested by the hosting team before use with students.

## Start here

| Project | What teams build | Typical audience | Activity length | Main engineering idea |
| --- | --- | ---: | ---: | --- |
| [HydroGrab](designs/hydrograb/README.md) | Water-powered tabletop pick-and-place arm | Grades 6–10 | 75–90 min | Force–displacement tradeoff and linkages |
| [Rescue Hoist](designs/rescue-hoist/README.md) | Hand-cranked two-stage gear winch | Grades 7–12 | 90–120 min | Gear ratio, torque, and friction |
| [Crank Critter](designs/crank-critter/README.md) | Crank-driven walking mechanism or automaton | Grades 5–10 | 45–75 min | Degrees of freedom, pivots, and kinematics |

## Design philosophy

Every project follows the same cycle: **make a mechanism → measure a result → change one variable → explain the physical reason.** A build is not presented as a validated scientific result; it is a controlled, safe demonstration and design challenge.

Projects are deliberately low-voltage or hand-powered. The common kit is reusable, while common craft materials can be replenished economically. See [procurement guidance](docs/PROCUREMENT.md) and [safety requirements](docs/SAFETY.md) before purchasing or running an event.

## Repository layout

```text
designs/       One folder per activity: BOM, assembly, challenge, and facilitator notes
assets/        Editable SVG mechanism diagrams
docs/          Common procurement, safety, and event-planning guidance
```

## Contributions

Please open an issue or pull request with a build photo, a measured result, a sourcing substitution, or a correction. Include the student age range, material version, configuration, and observed failure mode so that a proposed design can progress toward a verified one.

## License

Suggested: [CERN-OHL-S v2](https://ohwr.org/cern_ohl_s_v2.txt) for hardware documentation, paired with [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for written instructional material. Confirm the intended organizational licensing policy before adding license files.
