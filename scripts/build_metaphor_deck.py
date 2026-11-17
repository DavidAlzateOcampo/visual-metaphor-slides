#!/usr/bin/env python3
"""
Visual Metaphor Slides — Interactive HTML Deck Generator
Generates a zero-dependency, 16:9 interactive HTML presentation implementing
all 20 non-rectangular Visual Structural Metaphors across 5 geometric families,
compliant with modern-web-guidance (native <dialog closedby="any">, Invoker Commands,
Directional View Transitions, light-dark() color-scheme, and @starting-style top-layer animations).
"""

import argparse
from pathlib import Path


def build_showcase_html() -> str:
    template_path = Path(__file__).resolve().parent.parent / "templates" / "showcase_all_20_metaphors.html"
    return template_path.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Build Visual Metaphor HTML Presentation Deck")
    parser.add_argument(
        "--output",
        "-o",
        default=str(Path(__file__).resolve().parent.parent / "templates" / "showcase_all_20_metaphors.html"),
        help="Output HTML file path",
    )
    args = parser.parse_args()
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build_showcase_html(), encoding="utf-8")
    print(f"Generated 20-slide Visual Metaphor HTML Deck at: {out_path}")


if __name__ == "__main__":
    main()
