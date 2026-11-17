---
name: synergy-network-slides
description: >-
  Creates HTML/SVG presentation slides using Overlap, Synergy & Spatial
  Interconnection Visual Metaphors (Patterns 13-16): #13 The Overlapping Optical
  Lens (Luminous Venn), #14 The Constellation / Synaptic Neural Mesh, #15 The
  Magnetic Field / Dipole Dynamic, and #16 The Stepping-Stone Island Chain. Use
  for strategic sweet-spot intersections, multi-agent neural meshes, polarity
  tension balances, and organic milestone journeys.
---

# Overlap, Synergy & Spatial Interconnection (`synergy-network-slides`) — Patterns 13 to 16

Use this skill when the message focuses on **emergent value at intersections, decentralized multi-agent topologies, dynamic tension between two poles, or organic stepping-stone journeys**.

All SVG viewports use `viewBox="0 0 1200 620"`.

---

## 🔮 Pattern 13: The Overlapping Optical Lens (Luminous Venn)

### When to Use
- Finding the strategic sweet spot at the intersection of 3 domains (e.g., *Desirability × Feasibility × Viability*, or *Domain Expertise × Proprietary Data × Agentic Workflows*).
- Unlike flat Venn diagrams, each circle uses translucent radial gradients with `mix-blend-mode: screen` (on dark themes) or `multiply` (on light themes) so **overlapping regions physically brighten into an illuminated prism core**.

### Exact SVG + CSS Blueprint
- **Lens A (Top-Left)**: `cx="490", cy="245", r="175"` (Cyan radial tint)
- **Lens B (Top-Right)**: `cx="710", cy="245", r="175"` (Violet radial tint)
- **Lens C (Bottom-Center)**: `cx="600", cy="410", r="175"` (Emerald radial tint)
- **Central Luminous Nexus (`cx="600", cy="300"`)**: Highlighted with a glowing white-gold beacon and callout leader line for the **"Synergy Sweet Spot"**.

---

## ✨ Pattern 14: The Constellation / Synaptic Neural Mesh

### When to Use
- Multi-agent AI swarms, peer-to-peer data mesh architectures, knowledge graphs, or decentralized team topologies where value flows across weighted synaptic links rather than top-down org charts.

### Exact SVG Blueprint
- Place 8–10 nodes at organic non-grid coordinates across `(140..1060, 110..520)` with 3 node tiers:
  - **Hub Synapses (`r="28"`)**: 3 primary orchestrator/domain nodes.
  - **Specialist Nodes (`r="18"`)**: 4–5 specialized worker nodes.
  - **Edge Sensors (`r="10"`)**: Peripheral trigger nodes.
- Connect nodes via curved quadratic Bezier arcs (`M x1 y1 Q cx cy x2 y2`) where **stroke-width (`1px` to `4px`) and opacity (`0.25` to `0.9`) encode coupling strength**.

---

## 🧲 Pattern 15: The Magnetic Field / Dipole Dynamic

### When to Use
- Balancing two Necessary Opposites without a boxy pros/cons table:
  - *Centralized Governance (North Pole)* ↔ *Federated Speed & Agility (South Pole)*
  - *Exploration / R&D* ↔ *Exploitation / Core Margin*
  - *Human Judgment* ↔ *Autonomous Execution*

### Exact SVG Magnetic Flux Blueprint
- **Left Pole (Positive / North)**: `cx="280", cy="310", r="68"` (Cyan/Blue core)
- **Right Pole (Negative / South)**: `cx="920", cy="310", r="68"` (Amber/Rose core)
- **Curved Magnetic Field Loops**:
  - Upper Inner Flux: `M 335 270 C 480 140, 720 140, 865 270`
  - Upper Outer Flux: `M 310 245 C 450 40, 750 40, 890 245`
  - Lower Inner Flux: `M 335 350 C 480 480, 720 480, 865 350`
  - Lower Outer Flux: `M 310 375 C 450 580, 750 580, 890 375`
- Anchor equilibrium mechanism pills directly on the upper and lower flux lines to show *how* the organization maintains healthy tension.

---

## 🏝️ Pattern 16: The Stepping-Stone Island Chain

### When to Use
- Customer onboarding journeys, progressive legacy modernization roadmaps, or capability maturity milestones where each stone is an organic island pad along a fluid stream.

### Exact SVG Organic Pebble Blueprint
- **Winding Stream Guide Path**: `M 90 450 C 310 520, 420 160, 630 280 C 820 390, 920 140, 1110 170`
- **5 Organic Pebble Pads (`<path>` or tilted `<ellipse>` with layered inner rings)**:
  - Stone 1: `(150, 455)` — `rx="78" ry="44" rotate(-10)`
  - Stone 2: `(375, 345)` — `rx="82" ry="46" rotate(-22)`
  - Stone 3: `(600, 265)` — `rx="88" ry="50" rotate(12)`
  - Stone 4: `(825, 295)` — `rx="84" ry="48" rotate(-18)`
  - Stone 5: `(1045, 175)` — `rx="92" ry="52" rotate(-6)` (Illuminated Destination Island)
