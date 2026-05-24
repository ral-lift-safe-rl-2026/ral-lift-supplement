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

## Reproducing figures

From a clean checkout of the training codebase (not included here):

1. Train or obtain checkpoints: SAC-Value 2M prior, M4.1 warm-start 200k (paths in supplement Sec. A).
2. Run robustness evaluation: `python eval_robustness.py` (see project `docs/`).
3. Regenerate paper figures: `python scripts/paper_data_audit.py`.

Qualitative video: `python record_qualitative_episode.py --preset col_a|col_b|col_c|col_prior_nominal` then `python make_multimedia_video.py`.

## Privacy

No author names, emails, or institution-specific absolute paths in this repository.
