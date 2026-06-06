#!/usr/bin/env python3
"""Plot entry vs violation ambiguity figure for RA-L main text."""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def _robustness_m4_1() -> Path:
    for base in (ROOT / "data" / "robustness_m4_1", ROOT / "robustness_m4_1"):
        if (base / "robustness_summary.csv").is_file():
            return base
    raise FileNotFoundError("robustness_m4_1 CSVs not found under data/ or repo root")


def _figure_out() -> Path:
    paper = ROOT / "paper_latex" / "figures" / "fig9_entry_violation_ambiguity.png"
    if paper.parent.is_dir():
        return paper
    return ROOT / "scripts" / "fig9_entry_violation_ambiguity.png"


DATA_DIR = _robustness_m4_1()
SUMMARY = DATA_DIR / "robustness_summary.csv"
EPISODES = DATA_DIR / "robustness_episodes.csv"
OUT = _figure_out()

POLICIES = {
    "SACV_2M": ("SAC-Value prior", "#1f77b4", "o"),
    "M4_1_baseline": (r"M4.1 baseline", "#d62728", "s"),
    "M4_1_repl0": (r"M4.1 repl0", "#ff7f0e", "^"),
}


def load_summary() -> list[dict]:
    with SUMMARY.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def plot_scatter(rows: list[dict]) -> None:
    fig, ax = plt.subplots(figsize=(3.35, 2.6))
    sigmas = [0.0, 0.06]
    for key, (label, color, marker) in POLICIES.items():
        pts = []
        for sig in sigmas:
            r = next(
                x
                for x in rows
                if x["policy"] == key and abs(float(x["sigma"]) - sig) < 1e-9
            )
            entry = float(r["manip_enter_rate"]) * 100
            viol = float(r["violation_rate_mean"]) * 100
            pts.append((entry, viol))
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color=color, linewidth=1.2, alpha=0.85, zorder=1)
        ax.annotate(
            "",
            xy=pts[1],
            xytext=pts[0],
            arrowprops=dict(arrowstyle="->", color=color, lw=1.1, shrinkA=4, shrinkB=4),
        )
        ax.scatter(
            [p[0] for p in pts],
            [p[1] for p in pts],
            c=color,
            marker=marker,
            s=52 if marker == "o" else 46,
            label=label,
            edgecolors="white",
            linewidths=0.4,
            zorder=2,
        )
        ax.text(pts[0][0] + 1.5, pts[0][1] + 0.15, r"$\sigma{=}0$", fontsize=6.5, color=color)
        ax.text(pts[1][0] + 1.5, pts[1][1] + 0.15, r"$\sigma{=}6$", fontsize=6.5, color=color)

    ax.set_xlabel(r"Manipulation-entry rate $P(\mathrm{enter})$ [\%]")
    ax.set_ylabel(r"Mean violation rate [\%]")
    ax.set_xlim(45, 95)
    ax.set_ylim(0, 6.5)
    ax.grid(True, alpha=0.25, linewidth=0.6)
    ax.legend(loc="upper left", fontsize=7, framealpha=0.92)
    ax.set_title(r"Aggregate safety vs.\ accessibility under shift", fontsize=8.5)
    fig.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUT}")


def threshold_table(policy: str = "M4_1_baseline", sigma: float = 0.06) -> None:
  rows = [
      r
      for r in csv.DictReader(EPISODES.open(newline="", encoding="utf-8"))
      if r["policy"] == policy and abs(float(r["sigma"]) - sigma) < 1e-9
  ]
  print(f"\nEntry-threshold sensitivity ({policy} @ sigma={sigma}):")
  for th in (0.03, 0.05, 0.10):
      entered = [r for r in rows if float(r["manip_frac"]) > th]
      ent = len(entered) / len(rows) * 100
      succ = sum(1 for r in rows if float(r["success"]) > 0.5) / len(rows) * 100
      pse = (
          sum(1 for r in entered if float(r["success"]) > 0.5) / len(entered) * 100
          if entered
          else float("nan")
      )
      print(f"  thresh={th:.0%}  entry={ent:.1f}%  succ={succ:.1f}%  P(s|e)={pse:.1f}%")


def main() -> None:
    rows = load_summary()
    plot_scatter(rows)
    threshold_table()


if __name__ == "__main__":
    main()
