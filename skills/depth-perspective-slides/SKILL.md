---
name: depth-perspective-slides
description: >-
  Creates HTML/SVG presentation slides using Layered, Depth & Perspective Visual
  Metaphors (Patterns 17-20): #17 The Tip-of-the-Iceberg Cross Section, #18 The
  Isometric Layered Glass Sandwich, #19 The Spotlight Focal Aperture, and #20
  The Bridge / Chasm Crossing. Use when exposing hidden 90% architectural depth,
  3D stacked tech layers, deep-dive subsystem zoom-ins, or Current-to-Future
  State chasm crossings.
---

# Layered, Depth & Perspective Frameworks (`depth-perspective-slides`) — Patterns 17 to 20

Use this skill when the slide relies on **vertical depth, above-vs-below surface contrast, 3D isometric layer stacks, focal spotlighting, or spanning a structural gap**.

All SVG viewports use `viewBox="0 0 1200 620"`.

---

## 🧊 Pattern 17: The Tip-of-the-Iceberg Cross Section

### When to Use
- Exposing hidden engineering complexity, Total Cost of Ownership (TCO), compliance/security plumbing beneath a sleek consumer UI, or why "a simple 2-week feature" requires 90% foundational architecture.

### Exact SVG Cross-Section Blueprint
- **Glowing Waterline Horizon (`y="215"`)**:
  - Wave path `M 60 215 Q 330 202, 600 215 T 1140 215` with cyan surface shimmer and deep abyssal gradient (`#0B192C → #040814`) below `y=215`.
- **Visible Peak Above Water (10% — UI / Executive Outcomes)**:
  - Crystalline polygon `points="515,215 565,95 615,115 645,85 690,215"` in bright ice-cyan (`#E0F2FE` / `#38BDF8`).
- **Massive Submerged Structure Below Water (90% — Infrastructure / Data / Governance)**:
  - Faceted multi-depth polygon `points="515,215 350,310 310,445 430,565 610,590 795,555 885,420 830,290 690,215"` partitioned into 3 horizontal depth strata (`y=280`, `y=395`, `y=510`) with left/right sonar callout lines.

---

## 🥞 Pattern 18: The Isometric Layered Glass Sandwich

### When to Use
- 3 to 5 layer architectural tech stacks (*Layer 4: Autonomous UX / Agents* → *Layer 3: Semantic & Ontology Plane* → *Layer 2: Unified Lakehouse & Vector Store* → *Layer 1: Cloud Compute & Zero-Trust Mesh*) where vertical laser conduits pierce through every plane.

### Exact SVG Isometric Disc / Rhombus Blueprint
- Stack 4 isometric planes centered at `x="560"` at vertical heights `y = [145, 255, 365, 475]`.
- Each layer is a rounded isometric plate or dual-ring ellipse (`rx="270", ry="62"`) with translucent glass fill, glowing border rim, and a `12px` 3D thickness lip underneath.
- Pierce all 4 layers with 3 vertical glowing laser beams (`x = 430, 560, 690`) and intersection pulse rings at each plane.

---

## 🔦 Pattern 19: The Spotlight Focal Aperture

### When to Use
- Pivoting from a macro system overview into a **high-resolution deep dive on one critical module** while keeping peripheral modules softly visible in dimmed context (`opacity: 0.25`).

### Exact SVG Conical Spotlight Blueprint
- **Dimmed Peripheral Context Nodes**: 5 background architectural nodes across the canvas at `opacity="0.25"`.
- **Spotlight Emitter (`x="140", y="110"`)**: Precision optical lens origin casting an expanding conical light beam polygon `points="140,110 730,105 960,515 520,515"` filled with a translucent radial/linear light gradient.
- **Illuminated Focal Aperture (`cx="755", cy="325", r="175"`)**: Bright high-contrast circular magnifying ring containing the detailed internal sub-components (3–4 micro-nodes + internal feedback loop) at full clarity.

---

## 🌉 Pattern 20: The Bridge / Chasm Crossing

### When to Use
- Gap analysis, cloud/AI transformation roadmaps, migration execution plans, or showing how a strategic initiative bridges the chasm between **Current State (Legacy Pain)** and **Future State (Target Value)**.

### Exact SVG Suspension Chasm Blueprint
- **Left Cliff Plateau ("Current State — Legacy Silos")**: Polygon `points="60,340 330,340 375,600 60,600"` with dark slate fill and top plateau markers.
- **Right Cliff Plateau ("Future State — Autonomous Scale")**: Polygon `points="870,260 1140,260 1140,600 825,600"` elevated higher (`y=260` vs `y=340`) to signify upward transformation.
- **The Deep Chasm (`x: 330 → 870`)**: Labeled at the bottom (`y=555`) with the **Critical Risks / Blockers** avoided (e.g., *Data Drift, Security Gaps, Integration Debt*).
- **Glowing Arching Bridge (`x: 330 → 870`)**:
  - Main Suspension Arch: `M 320 340 C 490 150, 710 110, 880 260`
  - Deck Span: `M 320 340 Q 600 275, 880 260`
  - 4 Illuminated Bridge Pillar Nodes along the span representing the concrete execution phases that carry the organization across the gap.
