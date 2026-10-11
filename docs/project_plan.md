# Project Plan

## MVP

Build a web lab where users investigate an unknown BB84 channel scenario.

Inputs:

- Scenario: hidden or revealed.
- Number of transmitted qubits.
- Public sample size.
- Noise probability.
- Eve intercept probability.
- Random seed.

Outputs:

- Sifted-key count.
- Compared sample count.
- Error count.
- QBER.
- 95% confidence interval.
- Evidence interpretation.

## Scientific Model

Alice randomly chooses bits and bases. Bob randomly chooses measurement bases. Bits are retained only when Alice and Bob used the same basis.

Scenario behavior:

- Ideal: no extra disturbance.
- Intercept-resend: Eve chooses a random basis, measures, and resends. If Eve used the wrong basis, she can disturb the state.
- Noise: each transmitted result can flip with a configured probability, without assuming an attacker.

Important limitation:

Similar QBER values can come from different causes, especially with small samples. The system should present evidence, not declare certainty.

## Evidence Labels

- Low sample: "Data insufficient."
- Confidence interval overlaps normal/noise baseline: "Compatible with benign disturbance."
- High QBER with tighter interval: "Strong evidence of perturbation, cause unresolved."

## Demo Cases

1. Small sample, noisy channel: user may suspect Eve, but evidence is weak.
2. Intercept-resend, larger sample: QBER moves toward a stronger perturbation signal.
3. Noise tuned near Eve-like QBER: demonstrates ambiguity.

## Stretch Goals

- Add Qiskit circuit generation for each prepare-measure shot.
- Add likelihood comparison between scenarios.
- Add false-positive and detection-rate dashboard after repeated trials.
- Add a reveal mode for judges.

