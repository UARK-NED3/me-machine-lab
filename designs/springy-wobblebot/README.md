# Springy Wobblebot: vibrating creature

![Springy Wobblebot diagram](../../assets/springy-wobblebot.svg)

Build a small, expressive creature that travels by vibrating an unbalanced motor on spring legs. Its body is an ordinary plastic enclosure; its legs, feet, and “antennae” are catalog parts that can be reconfigured without shaping a custom chassis.

**Design status:** proposed; pilot validation required. Use a 3 V battery supply only.

## Bill of materials — one Wobblebot

| Item | Direct catalog specification | Qty. | Source |
| --- | --- | ---: | --- |
| Body | Small plastic project enclosure with lid | 1 | [McMaster: plastic enclosures](https://www.mcmaster.com/products/plastic-enclosures) |
| Legs | Four light compression springs, 20–40 mm free length | 4 | [McMaster: compression springs](https://www.mcmaster.com/products/compression-springs/) |
| Feet | Small rubber bumpers or soft vinyl caps | 4 | [McMaster: rubber bumpers](https://www.mcmaster.com/products/rubber-bumpers/) |
| Motor | 3 V DC motor with a 2–3 mm shaft | 1 | [Amazon: 3 V DC motor](https://www.amazon.com/s?k=3v+dc+motor+mini) |
| Eccentric mass | Small shaft collar sized to motor shaft; mount off-axis | 1 | [McMaster: shaft collars](https://www.mcmaster.com/products/shaft-collars/) |
| Power and switch | 2×AA holder, low-voltage switch, and insulated leads | 1 set | [Amazon: 2 AA battery holder switch](https://www.amazon.com/s?k=2+aa+battery+holder+with+switch) |
| Attachment hardware | Small screws, washers, cable ties, and hook-and-loop strap | assorted | [McMaster: cable ties](https://www.mcmaster.com/products/cable-ties/) |

## Assembly

1. Attach the four springs to the enclosure underside with screws/washers or cable ties through existing enclosure features. Add rubber feet to the spring ends.
2. Secure the motor to the top of the enclosure using a clamp or two cable ties; it must not rotate relative to the body.
3. Mount the small collar eccentrically on the motor shaft. Start with the collar close to the shaft axis and increase offset only after a low-speed test.
4. Connect the motor, switch, and 2×AA holder in series. Confirm the circuit runs at nominal 3 V; never use a wall supply for this activity.
5. Decorate using removable cable ties, colored labels, or hook-and-loop attachments. These must not contact the eccentric mass.
6. Run a 10 s trial on a smooth floor. Change one factor—spring stiffness, leg spread, eccentric offset, or foot material—and measure displacement and toppling frequency.

## Physics prompt

The rotating offset mass creates a periodic force with magnitude that scales approximately as \(F\approx m e \omega^2\), where \(m\) is eccentric mass, \(e\) is offset, and \(\omega\) is angular speed. Motion across the floor depends on friction and how vibration couples to the spring legs; it is not guaranteed to increase monotonically with offset.

## Success criteria

- No part of the eccentric mass contacts the body or a student’s hand.
- The bot remains upright for at least one 10 s trial.
- Teams record the configuration and measured travel distance, including trials that moved backwards or spun in place.
