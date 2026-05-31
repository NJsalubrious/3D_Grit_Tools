The shoulder is the part of a biped rig that humbles people. Everyone can wire a clean two-bone IK leg. Far fewer can make a clavicle rotate convincingly as the arm lifts, automatically, without the animator babysitting it. This early prototype goes after exactly that problem.

## The FK/IK limb logic first

Before the clavicle, the arm needs a limb solution that blends cleanly between FK and IK. That means duplicate chains, a blend driver, and a pole vector that doesn't flip. Get this wrong and the auto-clavicle has nothing stable to react to. The breakdown builds this foundational logic before touching the shoulder.

## Cracking the auto-clavicle

The clavicle is hard because it should respond to the arm without taking control away from the animator. The approach: drive a base rotation from the arm's position so the shoulder lifts naturally, then leave an additive layer on top so the animator can push or dial it back. **Automatic, but never locked.**

## A prototype, honestly

This is an early build, and it reads like one. The point of sharing it isn't a finished product; it's the reasoning, why the shoulder complex resists automation, and what a workable first solution looks like. The current framework's shoulder setup grew directly out of this experiment.
