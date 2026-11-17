---
name: organic-flow-slides
description: >-
  Creates HTML/SVG presentation slides using Organic, Flow & Convergence Visual
  Metaphors (Patterns 9-12): #9 The River Delta / Confluence Flow, #10 The Deep
  Root & Canopy Tree Architecture, #11 The Hourglass / Choke-Point Funnel, and
  #12 The DNA Double Helix Pipeline. Use when replacing blocky ETL diagrams,
  showing invisible infrastructure roots feeding visible business apps, filtering
  high-volume signals through a narrow bottleneck, or coupling two parallel tracks.
---

# Organic, Flow & Convergence Frameworks (`organic-flow-slides`) — Patterns 9 to 12

Use this skill when the slide represents **fluid convergence/divergence, biological root-to-canopy hierarchy, bottleneck curation, or tightly coupled dual tracks**.

All SVG viewports use `viewBox="0 0 1200 620"`.

---

## 🌊 Pattern 9: The River Delta / Confluence Flow

### When to Use
- Multi-source data ingestion into a unified lakehouse, post-merger system consolidation, or unified omnichannel routing (multiple meandering tributaries merging into a powerful central stream).

### Exact SVG Tributary Confluence Blueprint
- **4 Left-Hand Tributaries (`stroke-linecap="round"`)**:
  - Tributary 1 (Top): `M 80 110 C 260 110, 340 280, 560 310` (`stroke-width="10"`, cyan)
  - Tributary 2 (Upper-Mid): `M 80 235 C 250 235, 360 295, 560 310` (`stroke-width="12"`, sky blue)
  - Tributary 3 (Lower-Mid): `M 80 385 C 250 385, 360 325, 560 310` (`stroke-width="12"`, violet)
  - Tributary 4 (Bottom): `M 80 510 C 260 510, 340 340, 560 310` (`stroke-width="10"`, emerald)
- **Confluence Vortex Node (`cx="560", cy="310"`)**: Glowing circular confluence hub (`r="48"`).
- **Unified Main River Trunk (Right-Hand Output)**:
  - `M 560 310 C 740 310, 850 290, 1110 310` (`stroke-width="34"`, gradient blend of all 4 tributary colors with animated dashed flow particles overlaid).

---

## 🌳 Pattern 10: The Deep Root & Canopy Tree Architecture

### When to Use
- Connecting invisible foundational work (**Subterranean Roots**: Data Governance, Security, Cloud IAM, Schema Contracts) through the **Central Trunk** (Core Platform / Unified Engine) to visible outcomes (**Foliage Canopy**: Executive Dashboards, AI Copilots, Customer APIs, Revenue Products).

### Exact SVG Layout Blueprint
- **Horizon Ground Line (`y="365"`)**: Crisp horizontal soil horizon `M 100 365 L 1100 365` separating *"Visible Business Value (Canopy)"* above from *"Invisible Foundation (Root System)"* below.
- **Subterranean Taproots (`y: 365 → 575`)**: 4 curved root paths branching downward from `(600, 365)` to `(240, 540)`, `(460, 565)`, `(740, 565)`, and `(960, 540)`.
- **Central Trunk (`y: 365 → 230`)**: Sculpted organic trunk polygon narrowing and flaring from `(600, 365)` up to `(600, 230)`.
- **Expansive Canopy (`y: 60 → 240`)**: 4–5 overlapping translucent foliage orbs (`r="75"` to `r="95"`) spanning `x=260` to `x=940`, each holding a business capability badge.

---

## ⏳ Pattern 11: The Hourglass / Choke-Point Funnel

### When to Use
- GenAI RAG context filtering, quality assurance gates, signal-to-noise distillation, or capital allocation where **high-volume noisy inputs** pass through a **strict validation bottleneck** before fanning out into **high-value actions**.

### Exact SVG Hourglass Geometry (Horizontal or Vertical)
- **Upper/Left Wide Intake Pool**: `M 140 90 C 140 240, 535 250, 555 310` and `M 140 530 C 140 380, 535 370, 555 310`
- **The Glowing Throat / Choke-Point (`cx="600", cy="310"`)**: High-intensity glowing aperture ring (`r="42"`) labeled *"Quality / Governance Gate"*.
- **Lower/Right Distribution Fan**: Symmetrical expansion from `(645, 310)` fanning out to `(1060, 90)` and `(1060, 530)` with 4 clean output rays.

---

## 🧬 Pattern 12: The DNA Double Helix Pipeline

### When to Use
- Two distinct workstreams that **must stay synchronized at every milestone** (e.g., *Track A: Business Strategy* ↔ *Track B: Engineering Execution*, or *Model Capabilities* ↔ *AI Safety Guardrails*).

### Exact SVG Sinusoidal Double Helix Paths
- **Strand A (Cyan Wave)**:
  `d="M 80 190 C 210 190, 270 430, 400 430 C 530 430, 590 190, 720 190 C 850 190, 910 430, 1040 430"`
- **Strand B (Violet Wave - 180° Phase Shifted)**:
  `d="M 80 430 C 210 430, 270 190, 400 190 C 530 190, 590 430, 720 430 C 850 430, 910 190, 1040 190"`
- **Base-Pair Coupling Rungs**: Vertical connector lines with dual terminal nodes at `x = [140, 320, 480, 640, 800, 980]` and crossover synchronization badges at the 3 intersection nodes `(240, 310)`, `(560, 310)`, and `(880, 310)`.
