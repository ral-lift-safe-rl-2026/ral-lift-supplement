# Anonymous supplementary materials (RA-L)

This repository supports the double-blind RA-L submission on **manipulation-entry collapse** in safe robotic RL for contact-rich lifting.

## Contents

| Path | Description |
|------|-------------|
| `main.pdf` | Manuscript (IEEE two-column, anonymous) |
| `supplement.pdf` | Extended methods, figures, falsification, data notes (~10 pp) |
| `multimedia/multimedia.mp4` | Qualitative rollouts (≤2 min; also on PaperCept) |
| `multimedia/ReadMe.txt` | Multimedia description for PaperCept |
| `data/` | Evaluation CSVs for main robustness grids |
| `latex/` | Optional LaTeX sources (`paper_latex_ral/` + figures) |

## Reproducing figures

From a clean checkout of the training codebase (not included here to save space):

1. Train or obtain checkpoints: SAC-Value 2M prior, M4.1 warm-start 200k (paths in supplement Sec. A).
2. Run robustness evaluation: `python eval_robustness.py` (see project `docs/`).
3. Regenerate paper figures: `python scripts/paper_data_audit.py`.

Qualitative video frames: `python record_qualitative_episode.py --preset col_a|col_b|col_c|col_prior_nominal` then `python make_multimedia_video.py`.

## Citation

Anonymous submission — do not cite until published.

## Privacy

No author names, emails, or institution-specific absolute paths should appear in this repository.
