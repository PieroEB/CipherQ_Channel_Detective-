# Demo Cases

This file defines Piero's evidence-analysis demo cases. The goal is to show what the data supports without overstating the cause of the errors.

## Demo Message

Channel Detective does not announce "Eve is present" just because errors appear. It shows the observed QBER, the uncertainty from the public sample, and a cautious conclusion.

## Case 1 - Tiny Sample, Suspicious But Uncertain

Purpose: show that a small public sample can be misleading.

Suggested parameters:

- Scenario: `intercept`
- Transmitted qubits: `600`
- Public sample size: `24`
- Eve intercept probability: `1.0`
- Seed: `11`

Expected teaching point:

Even if the hidden scenario is intercept-resend, the public sample is too small for a confident claim. The correct conclusion is uncertainty, not certainty.

## Case 2 - Larger Sample, Strong Disturbance Evidence

Purpose: show how larger samples reduce uncertainty.

Suggested parameters:

- Scenario: `intercept`
- Transmitted qubits: `4000`
- Public sample size: `800`
- Eve intercept probability: `1.0`
- Seed: `11`

Expected teaching point:

The QBER estimate becomes more stable. The evidence supports "strong perturbation", but still does not identify the cause by itself.

## Case 3 - Noise-Only Channel That Looks Suspicious

Purpose: show that errors can come from a benign channel or equipment model.

Suggested parameters:

- Scenario: `noise`
- Transmitted qubits: `4000`
- Public sample size: `800`
- Noise probability: `0.20`
- Seed: `17`

Expected teaching point:

A noise-only model can produce a QBER that looks similar to an attack-like case. The system should avoid saying "Eve" when the observation is only "disturbance".

## Case 4 - Ideal Baseline

Purpose: provide a comparison case with no added attack or perturbation.

Suggested parameters:

- Scenario: `ideal`
- Transmitted qubits: `2000`
- Public sample size: `300`
- Seed: `23`

Expected teaching point:

The baseline should show no strong perturbation signal. This helps users understand what the error panel looks like before adding Eve or noise.

## Judge Script

1. Start with the tiny-sample case and ask: "Can we conclude there is an attacker?"
2. Point to the wide confidence interval and answer: "No. The data is too limited."
3. Increase the public sample size and show how uncertainty shrinks.
4. Show the noise-only case and ask: "Does a similar QBER prove Eve?"
5. Reveal that the suspicious-looking run can come from noise only.
6. Close with the main message: "The lab separates observation, hypothesis, and conclusion."

## Commands

Run prepared cases:

```bash
python3 -m src.channel_detective.evidence_lab --mode demo
```

Run sample-size sweep:

```bash
python3 -m src.channel_detective.evidence_lab --mode sweep --scenario intercept
```

