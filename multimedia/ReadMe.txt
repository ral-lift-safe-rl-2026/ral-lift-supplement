This video supports the RA-L paper on manipulation-entry collapse in safe
reinforcement learning for contact-rich robotic manipulation.

Content: robosuite Lift task with a Panda arm. Two policies from the same
unconstrained SAC-Value prior: (left) the 2M-step prior only; (right) phase-aware
constrained fine-tuning (M4.1). Side-by-side clips at sigma = 0 cm and 6 cm
(Gaussian xy object noise after each reset). At sigma = 6 cm, matched reset seeds
are used for fair comparison.

Purpose: illustrate manipulation-entry collapse. Under shift, M4.1 often fails
before sustained manipulation (hesitation, larger standoff) while the prior still
attempts contact-rich grasping and can complete the lift. A short metrics panel
summarizes success, manipulation-entry rate, and conditional success given entry.

No code, checkpoints, or hyperparameters are included in this attachment.
Extended experiments and reproducibility materials are in the anonymous supplement
repository cited in the paper.
