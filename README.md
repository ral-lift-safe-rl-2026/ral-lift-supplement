# Anonymous supplementary materials (RA-L)

External materials for the double-blind RA-L submission on **manipulation-entry collapse** in safe robotic RL for contact-rich lifting.

**Main manuscript:** submitted via RA-L PaperCept only — **not** hosted in this repository.

## Contents

| Path | Description |
|------|-------------|
| `supplement.pdf` | Extended methods, figures, falsification, data notes (~10 pp) |
| `multimedia/multimedia.mp4` | Qualitative rollouts (≤2 min; also on PaperCept) |
| `multimedia/ReadMe.txt` | Multimedia description for PaperCept |
| `data/` | Evaluation CSVs for main robustness grids |
| `scripts/plot_aggregate_ambiguity.py` | Regenerate main-text Fig.~9 (entry vs.\ violation) from `data/` |

## Reproducing figures

From a clean checkout of the training codebase (not included here):

1. Train or obtain checkpoints: SAC-Value 2M prior, M4.1 warm-start 200k (paths in supplement Sec. A).
2. Run robustness evaluation: `python eval_robustness.py` (see project `docs/`).
3. Regenerate paper figures: `python scripts/paper_data_audit.py`.

From **this repository only** (Fig.~9 / Sec.~5.4 aggregate-ambiguity panel):

```bash
python scripts/plot_aggregate_ambiguity.py
```

Writes `scripts/fig9_entry_violation_ambiguity.png` here, or `paper_latex/figures/` when run from the full training tree.

Qualitative video: `python record_qualitative_episode.py --preset col_a|col_b|col_c|col_prior_nominal` then `python make_multimedia_video.py`.

## Privacy

No author names, emails, or institution-specific absolute paths in this repository.
