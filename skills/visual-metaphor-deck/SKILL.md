---
name: visual-metaphor-deck
description: >-
  Master HTML presentation orchestrator and deck builder using 20 non-rectangular
  visual structural metaphor slide layouts (Planetary Orbit, Concentric Ripple,
  Onion Sphere, Polar Dial, Sigmoid S-Curve, Rollercoaster Slingshot, Archimedean
  Spiral, Rocket Booster, River Delta, Tree Root & Canopy, Hourglass Funnel, DNA
  Double Helix, Luminous Venn Lens, Constellation Mesh, Magnetic Dipole, Stepping-Stone
  Islands, Iceberg Cross-Section, Isometric Glass Stack, Spotlight Aperture, and
  Chasm Bridge). Triggers on "/metaphor-deck", "visual metaphor presentation",
  "HTML presentation without rectangular cards", "create metaphor slides", or when
  designing multi-slide HTML presentations where slide geometry mirrors message logic.
---

# Visual Metaphor Deck — Master Orchestrator & HTML Presentation Engine

Breaks out of standard rectangular bullet cards and 2x2 grids by mapping every slide's narrative logic to one of **20 Visual Structural Metaphors** across 5 geometric families, rendered in self-contained interactive 16:9 HTML + SVG that strictly complies with **`modern-web-guidance`**.

---

## 🧭 The 20 Visual Structural Metaphors & Skill Routing Matrix

When planning a deck or single slide, match the **logical argument** of each slide to its geometric metaphor and load the corresponding specialized skill for exact SVG/CSS coordinates and templates:

### Family 1: Core Hub & Radial Metaphors (`hub-radial-slides`)
| # | Metaphor Name | Core Geometry | Best Used For |
|---|---|---|---|
| **1** | **Gravitational Planetary Orbit** | Illuminated core sphere + tilted elliptical SVG orbital rings + floating satellite nodes scaled by priority | Platform ecosystems, core engine architectures, peripheral service dependencies |
| **2** | **Concentric Ripple / Target Wave** | Expanding circular wave bands radiating outward from a focal origin | Blast radius, adoption impact, `Core → Extended → Market` rollout phases |
| **3** | **Nested Russian-Doll (Onion Sphere)** | Translucent cutaway concentric spheres revealing inner layers like a 3D planetary core | Defense-in-depth security, data governance maturity, foundational tech layers |
| **4** | **Polar Clock / Dial Matrix** | 360° circular radar sweep partitioned into curved SVG annular sector wedges | Continuous 24/7 monitoring, lifecycle stages, holistic domain coverage audits |

### Family 2: Trajectory, Growth & Exponential Momentum (`trajectory-momentum-slides`)
| # | Metaphor Name | Core Geometry | Best Used For |
|---|---|---|---|
| **5** | **Sigmoid (S-Curve) Inflection Path** | Smooth cubic Bezier S-curve (`M ... C ...`) with flat origin, steep inflection point, and upper asymptote | Digital transformation, phase transitions, compounding efficiency, AI adoption |
| **6** | **Rollercoaster / Momentum Slingshot** | Dipping Bezier trough ("J-Curve valley") that slingshots into a steep upward vector | Short-term investment vs. long-term ROI, refactoring tech debt before hyper-scaling |
| **7** | **Ascending Archimedean Spiral** | Helical 3D perspective ribbon coiling upward and widening with each loop | Agile engineering sprints, flywheel feedback loops, capability compounding |
| **8** | **Rocket Booster Multi-Stage Vector** | Diagonal escape trajectory with detachable booster stage capsules and ignition nodes | Multi-year strategic horizons (H1/H2/H3), catalysts fueling the next growth leap |

### Family 3: Organic, Flow & Convergence Frameworks (`organic-flow-slides`)
| # | Metaphor Name | Core Geometry | Best Used For |
|---|---|---|---|
| **9** | **River Delta / Confluence Flow** | Meandering Bezier tributaries converging into a wide central trunk (or branching delta) | Data ingestion pipelines, multi-source ETL to lakehouse, post-M&A consolidation |
| **10** | **Deep Root & Canopy Tree** | Subterranean taproots below ground line + structural trunk + expansive organic canopy | Governance/infrastructure (roots), core platform (trunk), business apps (canopy) |
| **11** | **Hourglass / Choke-Point Funnel** | Wide upper intake pool narrowing through an illuminated throat into a lower distribution fan | GenAI prompt/context filtering, data curation, raw signals → executive decisions |
| **12** | **DNA Double Helix Pipeline** | Two phase-shifted sinusoidal waves (`sin(x)` & `-sin(x)`) linked by rung bridges | Coupled parallel tracks: Business Strategy ↔ Tech Execution, Governance ↔ Analytics |

### Family 4: Overlap, Synergy & Spatial Interconnection (`synergy-network-slides`)
| # | Metaphor Name | Core Geometry | Best Used For |
|---|---|---|---|
| **13** | **Overlapping Optical Lens (Luminous Venn)** | Frosted-glass translucent circles using additive glow (`mix-blend-mode: screen`) at intersections | Strategic sweet spot, cross-functional synergy, competitive differentiation |
| **14** | **Constellation / Synaptic Neural Mesh** | Scattered luminous nodes linked by weighted dashed Bezier synapses | Multi-agent workflows, decentralized data mesh, organic organizational networks |
| **15** | **Magnetic Field / Dipole Dynamic** | Opposing charged poles (North/South) connected by arched SVG magnetic flux loops | Polarity & tension models: Central Control vs. Local Agility, Speed vs. Governance |
| **16** | **Stepping-Stone Island Chain** | Organic pebble-shaped SVG morph pads arranged along a winding S-path | Customer journeys, product roadmaps, progressive legacy modernization milestones |

### Family 5: Layered, Depth & Perspective Frameworks (`depth-perspective-slides`)
| # | Metaphor Name | Core Geometry | Best Used For |
|---|---|---|---|
| **17** | **Tip-of-the-Iceberg Cross Section** | Crisp glowing waterline; compact 10% visible peak above, massive 90% submerged polygon below | Exposing hidden complexity, Total Cost of Ownership (TCO), backend pipelines behind UI |
| **18** | **Isometric Layered Glass Sandwich** | 3D tilted translucent elliptical/rounded discs (`rotateX(60deg)`) pierced by vertical laser beams | Modern tech stacks (Infrastructure → Data → Semantic Layer → AI Agents → UX) |
| **19** | **Spotlight Focal Aperture** | Darkened canvas pierced by an angled conical light beam illuminating a zoomed-in subsystem | Architectural deep-dives, root-cause zoom-ins, pivoting from vision to module detail |
| **20** | **Bridge / Chasm Crossing** | Left ("Current State") and Right ("Future State") cliff plateaus spanned by a glowing suspension arch | Gap analysis, cloud/AI migration roadmaps, overcoming critical operational blockers |

---

## 🌐 Modern Web Guidance Architecture Built Into the Shell

Every HTML deck produced by this plugin implements the latest Web Baseline standards and fallbacks from `modern-web-guidance`:

1. **System-Aware Color Scheme & 4 Executive Themes (`dark-mode`, `dark-mode-toggle`)**:
   - Declares `<meta name="color-scheme" content="light dark">` in `<head>` with an inline FOUC-prevention script.
   - Sets `color-scheme: light dark` on `:root` mapped to `:has(> head > meta[name="color-scheme"][content="dark"|"light"])` and uses `light-dark()` tokens with `@media (prefers-color-scheme: dark)` fallbacks.
   - Supports system-aware light/dark switching plus 4 named presentation palettes (`executive-dark`, `midnight-cobalt`, `editorial-light`, `warm-parchment`).
2. **Directional View Transitions & Reduced Motion (`directional-navigation-transitions`, `motion`)**:
   - Navigates between slides via `document.startViewTransition({ update, types: [direction] })` (`'forward'` or `'backward'`) with a graceful fallback when `!document.startViewTransition`.
   - Animates `html:active-view-transition-type(forward|backward)` using compositor-friendly `transform: translateX(...)` keyframes and non-linear `cubic-bezier(0.16, 1, 0.3, 1)` timing.
   - Disables spatial slide transitions when `@media (prefers-reduced-motion: reduce)` is active and opts into spatial scaling only inside `@media (prefers-reduced-motion: no-preference)`.
3. **Declarative Top-Layer `<dialog>` Overview Grid (`dialog`, `light-dismiss-a-dialog`, `declarative-dialog-popover-control`, `prevent-page-scroll-under-modal-dialog`, `animate-to-from-top-layer`)**:
   - Uses a native `<dialog id="overviewModal" closedby="any" aria-labelledby="overviewTitle">` without redundant `role="dialog"` or `aria-modal`.
   - Controlled declaratively via `<button type="button" commandfor="overviewModal" command="show-modal">` and `command="close"`, with conditional `invokers-polyfill` loading (`if (!('commandForElement' in HTMLButtonElement.prototype))`) and a bounding-rect `closedby` fallback (`if (!('closedBy' in HTMLDialogElement.prototype))`).
   - Prevents background scroll chaining via `dialog:modal { overscroll-behavior: contain; }` and `dialog::backdrop { overflow: hidden; overscroll-behavior: contain; }`.
   - Animates top-layer entry and exit using `@starting-style`, `transition-behavior: allow-discrete` (declared separately after `transition`), `overlay`, and the `closeTopLayer()` `getAnimations()` exit fallback.

### Reference Showcase File
To inspect or copy working code for all 20 metaphors at once, read:
- `C:\Users\LENOVO\.gemini\config\plugins\visual-metaphor-slides\templates\showcase_all_20_metaphors.html`
- `C:\Users\LENOVO\.gemini\config\plugins\visual-metaphor-slides\scripts\build_metaphor_deck.py`
