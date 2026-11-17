---
name: hub-radial-slides
description: >-
  Creates HTML/SVG presentation slides using Core Hub & Radial Visual Metaphors
  (Patterns 1-4): #1 The Gravitational Planetary Orbit, #2 The Concentric Ripple
  / Target Wave, #3 The Nested Russian-Doll (Onion Sphere), and #4 The Polar Clock
  / Dial Matrix. Use when visualizing platform ecosystems, blast radiuses,
  defense-in-depth security layers, data governance maturity, or 24/7 continuous
  lifecycle coverage without rectangular cards.
---

# Core Hub & Radial Metaphors (`hub-radial-slides`) — Patterns 1 to 4

Use this skill when the slide's message revolves around **central gravity, radiating impact, concentric containment, or cyclical 360° coverage**.

All SVG viewports are standardized to `viewBox="0 0 1200 620"` inside a 16:9 slide container (`1600×900` scaled viewport).

---

## 🪐 Pattern 1: The Gravitational Planetary Orbit

### When to Use
- Platform ecosystems, core engine architectures, microservices orbiting a shared kernel, or showing how peripheral products depend on a central system.
- Priority is encoded by **orbital distance** (inner orbit = critical coupling; outer orbit = peripheral extension) and **sphere radius**.

### SVG + HTML Structural Blueprint
```html
<section class="slide" data-metaphor="1-planetary-orbit">
  <header class="slide-header">
    <span class="metaphor-badge">01 · Gravitational Planetary Orbit</span>
    <h1>Core Platform Ecosystem &amp; Orbital Dependencies</h1>
    <p class="subtitle">Distance from the illuminated core encodes coupling tightness and service criticality</p>
  </header>
  <div class="canvas-stage">
    <svg viewBox="0 0 1200 620" class="metaphor-svg">
      <defs>
        <radialGradient id="coreGlow" cx="35%" cy="35%" r="65%">
          <stop offset="0%" stop-color="#67E8F9" />
          <stop offset="45%" stop-color="#0284C7" />
          <stop offset="100%" stop-color="#0F172A" />
        </radialGradient>
        <filter id="glow1" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="14" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>

      <!-- Tilted Elliptical Orbital Rings -->
      <g transform="translate(560, 320) rotate(-14)">
        <ellipse cx="0" cy="0" rx="220" ry="95" fill="none" stroke="var(--accent-cyan)" stroke-width="1.5" stroke-dasharray="6 6" opacity="0.55" />
        <ellipse cx="0" cy="0" rx="360" ry="155" fill="none" stroke="var(--accent-violet)" stroke-width="1.5" stroke-dasharray="8 8" opacity="0.45" />
        <ellipse cx="0" cy="0" rx="500" ry="215" fill="none" stroke="var(--accent-emerald)" stroke-width="1.5" stroke-dasharray="4 10" opacity="0.35" />
      </g>

      <!-- Central Illuminated Core Sphere -->
      <circle cx="560" cy="320" r="95" fill="url(#coreGlow)" filter="url(#glow1)" opacity="0.25" />
      <circle cx="560" cy="320" r="72" fill="url(#coreGlow)" stroke="#BAE6FD" stroke-width="2" />
      <text x="560" y="314" text-anchor="middle" class="svg-title">CORE KERNEL</text>
      <text x="560" y="336" text-anchor="middle" class="svg-sub">Unified State &amp; Auth</text>

      <!-- Orbit 1 Satellites (Inner - High Priority) -->
      <g class="satellite-node" transform="translate(355, 295)">
        <circle r="34" fill="#0EA5E9" fill-opacity="0.25" stroke="#38BDF8" stroke-width="2.5" />
        <circle r="8" fill="#38BDF8" />
        <text x="0" y="-46" text-anchor="middle" class="node-title">Identity Mesh</text>
        <text x="0" y="-28" text-anchor="middle" class="node-caption">Zero-trust token broker</text>
      </g>

      <g class="satellite-node" transform="translate(768, 342)">
        <circle r="30" fill="#0EA5E9" fill-opacity="0.25" stroke="#38BDF8" stroke-width="2.5" />
        <circle r="7" fill="#38BDF8" />
        <text x="0" y="52" text-anchor="middle" class="node-title">Event Bus</text>
        <text x="0" y="70" text-anchor="middle" class="node-caption">Sub-ms pub/sub stream</text>
      </g>

      <!-- Orbit 2 Satellites (Mid - Domain Engines) -->
      <g class="satellite-node" transform="translate(265, 455)">
        <circle r="26" fill="#A855F7" fill-opacity="0.22" stroke="#C084FC" stroke-width="2" />
        <circle r="6" fill="#C084FC" />
        <text x="0" y="46" text-anchor="middle" class="node-title">Billing Engine</text>
        <text x="0" y="64" text-anchor="middle" class="node-caption">Usage metering</text>
      </g>

      <g class="satellite-node" transform="translate(860, 165)">
        <circle r="28" fill="#A855F7" fill-opacity="0.22" stroke="#C084FC" stroke-width="2" />
        <circle r="6" fill="#C084FC" />
        <text x="0" y="-40" text-anchor="middle" class="node-title">AI Copilot Runtime</text>
        <text x="0" y="-22" text-anchor="middle" class="node-caption">Context orchestration</text>
      </g>

      <!-- Orbit 3 Satellites (Outer - Edge & Ecosystem) -->
      <g class="satellite-node" transform="translate(105, 225)">
        <circle r="22" fill="#10B981" fill-opacity="0.2" stroke="#34D399" stroke-width="1.8" />
        <circle r="5" fill="#34D399" />
        <text x="0" y="-34" text-anchor="middle" class="node-title">Partner Webhooks</text>
      </g>

      <g class="satellite-node" transform="translate(1020, 395)">
        <circle r="22" fill="#10B981" fill-opacity="0.2" stroke="#34D399" stroke-width="1.8" />
        <circle r="5" fill="#34D399" />
        <text x="0" y="42" text-anchor="middle" class="node-title">External SDKs</text>
      </g>
    </svg>
  </div>
</section>
```

---

## 🎯 Pattern 2: The Concentric Ripple / Target Wave

### When to Use
- Blast radius analysis, product rollout waves (`Internal Alpha → Design Partners → Enterprise GA → Global Ecosystem`), or compounding market reach.
- Place the origin on the **left-center (`cx="220", cy="310"`)** so expanding concentric wave arcs sweep rightward across the slide canvas, giving generous space for curved band callouts.

### SVG Geometry Formula
- Origin at `(220, 310)` with radii `R = [95, 230, 380, 540, 710]`.
- Place curved callout badges along a 12° upward radial ray or stagger them across angles `[-22°, -7°, +8°, +22°]`.

---

## 🧅 Pattern 3: The Nested Russian-Doll (Onion Sphere)

### When to Use
- Defense-in-depth cybersecurity, data governance maturity layers, or foundational kernel architecture inside customer-facing shells.
- Uses **bottom-anchored or cutaway concentric spheres** (`cy = center + offset`) with clip-path cutaways or stepped transparency so every inner layer rests visibly inside the outer shell.

### Assembly Tip
- Use 4 concentric circles with decreasing radii `R = [250, 190, 130, 70]` where `cy` shifts slightly downward (`cy = 300 + (250 - R) * 0.35`) to create a 3D nested bowl/orb effect, connected via horizontal leader lines to floating pill callouts on the left and right.

---

## 🧭 Pattern 4: The Polar Clock / Dial Matrix

### When to Use
- 24/7 continuous operations, DevSecOps infinite lifecycle, or 6–8 domain coverage audits where every sector belongs to an unbroken circular whole.

### SVG Annular Wedge Formula
To compute an annular sector wedge between inner radius $r_1$ and outer radius $r_2$ from angle $\theta_1$ to $\theta_2$ (in degrees, where $0^\circ$ is 12 o'clock):
```javascript
// Polar to Cartesian helper:
// x = cx + r * Math.sin(rad), y = cy - r * Math.cos(rad)
```
Leave a `3°–4°` angular gap between adjacent wedges so each sector floats like a precision radar dial segment.
