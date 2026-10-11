# Evidence Layer Contract

This document explains how Piero's evidence-analysis layer connects with the simulator, backend, Qiskit work, and future UI.

## Input Fields

The evidence layer expects a simulation case with:

- `label`: human-readable case name.
- `scenario`: one of `ideal`, `intercept`, or `noise`.
- `transmitted`: number of BB84 transmissions to simulate.
- `public_sample_size`: number of sifted bits publicly compared for error estimation.
- `noise_probability`: probability of a noise flip in the noise scenario.
- `eve_intercept_probability`: probability that Eve intercepts a transmission in the intercept scenario.
- `seed`: optional random seed for reproducible demos.

## Output Fields

The evidence layer returns:

- `scenario`: scenario used by the simulator.
- `transmitted`: number of attempted transmissions.
- `sifted`: number of bits kept after Alice and Bob compare bases.
- `sample_size`: number of sifted bits used for public comparison.
- `errors`: number of disagreements in the public sample.
- `qber`: observed quantum bit error rate as a decimal.
- `ci_low`: lower bound of the 95% confidence interval.
- `ci_high`: upper bound of the 95% confidence interval.
- `uncertainty_width`: `ci_high - ci_low`.
- `conclusion`: cautious interpretation text.

## Integration Notes For Boris

If a backend/API is added, the response should preserve these fields so the UI can display QBER, confidence interval, uncertainty width, and conclusion without recalculating core statistics.

The UI can format:

- `qber * 100` as a percentage.
- `ci_low * 100` and `ci_high * 100` as a range.
- `uncertainty_width * 100` as percentage points.

## Integration Notes For Adrian

If the simulator is replaced or extended with Qiskit-backed runs, keep the same evidence output fields.

The evidence layer does not need to know whether measurements came from:

- the current lightweight simulator,
- a Qiskit local simulator,
- or a Qollab/IonQ simulator path.

It only requires sifted counts, sample errors, QBER, and sample size.

## Language Rules

Use:

- "Observed error rate"
- "Evidence of perturbation"
- "Compatible with noise or attack-like disturbance"
- "Cause unresolved"
- "Data insufficient"

Avoid:

- "Eve detected"
- "Attack confirmed"
- "Secure channel proven"
- "No attacker exists"

## Current Implementation

Current code:

- `src/channel_detective/evidence_lab.py`
- `src/channel_detective/bb84_simulator.py`

Current test command:

```bash
python3 -m unittest discover -s tests
```

