---
name: trajectory-momentum-slides
description: >-
  Creates HTML/SVG presentation slides using Trajectory, Growth & Exponential
  Momentum Visual Metaphors (Patterns 5-8): #5 The Sigmoid (S-Curve) Inflection
  Path, #6 The Rollercoaster / Momentum Slingshot, #7 The Ascending Archimedean
  Spiral, and #8 The Rocket Booster Multi-Stage Vector. Use when showing phase
  transitions, J-curve investment troughs before ROI, iterative flywheel sprints,
  or multi-stage Horizon 1/2/3 strategic trajectories.
---

# Trajectory, Growth & Exponential Momentum (`trajectory-momentum-slides`) — Patterns 5 to 8

Use this skill when the narrative is driven by **velocity, inflection points, temporary dips before hyper-growth, cyclical upward compounding, or multi-stage propulsion**.

All SVG viewports use `viewBox="0 0 1200 620"`.

---

## 📈 Pattern 5: The Sigmoid (S-Curve) Inflection Path

### When to Use
- Phase transitions, digital transformation, AI adoption maturity, shifting from legacy plateau through an inflection point into hyper-growth and eventual market asymptote.

### Exact SVG Cubic Bezier Geometry
- **Main S-Curve Path**: `d="M 90 500 C 420 500, 480 480, 600 300 C 720 120, 790 100, 1110 100"`
- **Area Fill Under Curve**: Duplicate path closed down to `L 1110 550 L 90 550 Z` with a vertical linear gradient (`opacity: 0.18 → 0.0`).
- **4 Key Milestone Nodes Along the S-Curve**:
  1. **Origin / Incubation (`x=190, y=496`)**: Flat foundation, high latency, R&D experimentation.
  2. **The Tipping Point (`x=465, y=425`)**: Architecture unlock, unit economics cross threshold.
  3. **Sigmoid Hyper-Growth (`x=635, y=248`)**: Steepest slope — compounding automation & network effects.
  4. **Dominance Asymptote (`x=980, y=104`)**: Market saturation & next S-curve jump-off.

---

## 🎢 Pattern 6: The Rollercoaster / Momentum Slingshot (J-Curve)

### When to Use
- Explaining why short-term investment cost, refactoring, or organizational restructuring creates a temporary dip ("The Trough of Transformation") that builds kinetic energy for explosive upward ROI.

### Exact SVG Path Blueprint
- **Baseline Horizon (Status Quo)**: Dashed horizontal line `M 80 370 L 1120 370` labeled *"Linear Status Quo (Stagnant)"*.
- **Slingshot Trajectory Curve**:
  `d="M 90 350 C 220 350, 290 535, 440 535 C 610 535, 720 110, 1090 85"`
- **Key Anchors**:
  - `x=140, y=355`: **Phase 1 — Architectural Refactor Kickoff**
  - `x=440, y=535`: **Phase 2 — Maximum Investment Trough** (Highlight with a glowing amber kinetic compression ring)
  - `x=675, y=335`: **Phase 3 — Breakeven Slingshot** (Crosses above status-quo line at high velocity)
  - `x=1030, y=92`: **Phase 4 — 10x Compounding Velocity**

---

## 🌀 Pattern 7: The Ascending Archimedean Spiral

### When to Use
- Iterative engineering sprints, continuous learning loops, or flywheel growth where each revolution repeats a cycle (`Sense → Decide → Act → Learn`) at a **higher altitude and wider radius**.

### Exact SVG Helical Ribbon Blueprint
Stack 3 ascending elliptical loops connected by smooth upward back-ribbons:
- **Loop 1 (Foundation Cycle - Bottom, Narrow)**: Center `(600, 480)`, `rx="170", ry="48"`
- **Loop 2 (Expansion Cycle - Middle, Wider)**: Center `(600, 325)`, `rx="280", ry="68"`
- **Loop 3 (Autonomous Scale - Top, Widest)**: Center `(600, 165)`, `rx="400", ry="85"`
- Connect the right tangent of Loop $k$ to the left tangent of Loop $k+1$ with an upward cubic Bezier ribbon (`stroke-width="8"`), and place a glowing vertical central axis (`x1="600" y1="550" x2="600" y2="60"`) through the core of the helix.

---

## 🚀 Pattern 8: The Rocket Booster Multi-Stage Vector

### When to Use
- Multi-year strategic horizons (`Horizon 1: Core Engine`, `Horizon 2: Adjacent Expansion`, `Horizon 3: Autonomous Ecosystem`) showing how each stage detaches after propelling the next leap.

### Exact SVG Multi-Stage Blueprint
- **Curved Escape Trajectory**: `d="M 100 520 Q 480 440, 1080 95"`
- **3 Angled Capsule Stages Along the Trajectory**:
  - **Stage I Booster (`translate(240, 475) rotate(-14)`)**: Rounded capsule (`width="210" height="74" rx="37"`), cyan glow + exhaust plume rings at rear.
  - **Stage II Sustainer (`translate(575, 345) rotate(-24)`)**: Rounded capsule (`width="220" height="74" rx="37"`), violet glow + ignition separation ring.
  - **Stage III Orbital Payload (`translate(915, 165) rotate(-32)`)**: Sleek nose-cone capsule (`width="230" height="74" rx="37"`), emerald/gold glow reaching orbital insertion.
