Facial rigging is where most pipelines quietly fall apart. The bones are easy. The problem is the dozens of corrective and expressive shapes that have to be sculpted, named, and wired without a single typo breaking the whole face. This breakdown automates the part humans get wrong: generation and wiring.

## One input shape, a full suite out

Instead of hand-sculpting every blendshape, the tool takes a single clean input and generates the standard suite from it, brows, lids, jaw, lip corners, and the in-betweens that sell real motion. You sculpt the intent once; the system produces the variants and keeps the naming consistent.

## Driving bones with shapes, not the other way around

The interesting move here is the direction of control. Rather than animating bones and hoping the deformation reads, the generated blendshapes **drive** the underlying bone structure through drivers. The animator works in expressive, readable controls; the bones follow.

> Consistency is the whole game. A facial rig with one mislabeled target is a facial rig that breaks on the worst possible frame.

## Where it still needs a human

Automation gets you a working, consistent base in minutes. It does not get you a *performance*. The art direction, the asymmetry, the specific way a character sneers, that stays with the artist. The tool just removes the hours of mechanical setup standing between you and that work.
