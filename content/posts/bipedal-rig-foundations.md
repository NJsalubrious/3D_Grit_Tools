Most auto-riggers fail in the same place: they treat the skeleton as a finished product instead of a foundation. They generate a clean hierarchy, hand it to an animator, and discover three weeks later that the spine can't arc, the hips fight the IK, and the whole thing has to come apart. This first pass is about getting the architecture right before a single control curve is drawn.

## Hierarchy before features

A production bipedal rig lives or dies on its parenting order. Before any IK, before any constraints, the bone chain has to read like a real load path: pelvis at the root, spine stacked above it, the limb chains hanging off clear shoulder and hip anchors. If the hierarchy is wrong, every feature you bolt on afterward inherits the mistake.

The framework builds this from a small set of locators rather than guessing from the mesh. You place the joints; the system reads intent. That separation, **you decide structure, the tool handles the tedium**, is the whole philosophy.

## Why IK/FK switching is a foundation concern

Animators expect to blend between IK and FK on the same limb without re-keying the pose. That isn't a feature you sprinkle on at the end; it changes how the limb chain is built. The duplicate chains and the blend driver have to exist from the first generation pass, or you end up rebuilding the arm twice.

## What this pass does not solve

This is foundations, not the finished rig. No facial setup, no soft-body, no corrective shapes yet. What it gives you is a skeleton that won't betray you later: clean names, predictable orientations, and a hierarchy you can keep building on.

The breakdown above walks through the generation step by step.
