# Channel Detective - Implementation Workflows

Read `context.md` and `AGENTS.md` first. Use `docs/project_plan.md` and `docs/team_roles.md` for current scope and ownership.

These workflows describe planned work, not completed capabilities.

## Shared starting point

Before building components independently:

- Agree on the simulation request and response fields.
- Fix names for the three scenarios: `ideal`, `intercept`, and `noise`.
- Decide how random seeds are handled in demos.
- Decide whether the first UI runs fully in Python/Qollab or through a local web stack.
- Identify unresolved contract details before implementing dependent code.

Owners can work concurrently once these agreements are in place.

## 1. BB84 and Qiskit protocol model

Owner: Adrian.

### Build

1. Define how Alice bits, Alice bases, Bob bases, Eve basis choices, and noise are generated.
2. Implement or validate Qiskit prepare-measure circuits for `Z` and `X` bases.
3. Implement intercept-resend as Eve measurement followed by resend.
4. Keep scenario parameters explicit.
5. Return raw enough data for classical sifting and analysis.

### Verify

- Matching bases agree in the ideal case.
- Mismatched bases behave probabilistically.
- Intercept-resend introduces disturbance under the stated assumptions.
- Noise-only errors can occur without Eve.
- Circuit basis mapping is documented and tested.

### Hand off

Provide the protocol implementation, assumptions, test results, and any backend limitations.

## 2. Backend and integration

Owner: Boris.

### Build

1. Define a simulation request schema.
2. Define a response schema with counts, rates, uncertainty, and scenario metadata.
3. Expose a clean function or API endpoint for the UI.
4. Validate inputs, including sample size and probability ranges.
5. Keep seeded demo runs reproducible.
6. Add automated tests around the response contract.

### Verify

- Invalid inputs fail clearly.
- Results are reproducible with a fixed seed.
- API or function output matches the documented schema.
- Tests can be run from a fresh clone.

### Hand off

Provide run commands, response examples, actual test results, and integration notes for the UI.

## 3. Evidence, statistics, and visualization

Owner: Piero.

### Build

1. Calculate QBER from public sample errors.
2. Compute a confidence interval for the observed error rate.
3. Label conclusions cautiously.
4. Show how uncertainty changes with sample size.
5. Design false-alarm and ambiguity examples.

### Verify

- Small samples produce visibly wide uncertainty.
- Larger samples narrow the interval.
- Noise-only and intercept-resend can be configured to appear similar.
- The interface never says "Eve is present" solely because errors exist.

### Hand off

Provide chart components or notebook prototypes, demo cases, and wording for judge-facing explanations.

## 4. Interface and demo experience

Owners: Boris and Piero, with Adrian reviewing scientific language.

### Build

1. Provide controls for scenario, hidden/reveal mode, transmitted qubits, sample size, noise probability, Eve probability, and seed.
2. Show experiment flow: Alice prepares, Bob measures, bases are compared, sample is analyzed.
3. Present QBER, error count, confidence interval, and cautious conclusion.
4. Include a reveal button or judge-demo reveal step.
5. Keep UI accessible and readable.

### Verify

- Text does not overlap at mobile or desktop sizes.
- Controls have labels.
- Color is not the only way information is communicated.
- Demo cases can be reproduced quickly.

### Hand off

Provide the runnable entry point, screenshots or screen recording notes, and any unresolved UI limitations.

## 5. Integration checkpoint

Owners: all three.

Connect one scenario through the complete path:

Simulation request -> BB84/protocol logic -> sifting -> statistics -> explanation -> reveal.

Confirm that:

- All components use the same scenario definitions.
- QBER is calculated from sifted public-sample bits.
- Confidence intervals are calculated from the compared sample size.
- The UI distinguishes observation, hypothesis, and conclusion.
- A fresh clone can reproduce documented behavior.

Integrate this small example before adding features.

## 6. Publication and submission

Adrian coordinates submission.
Boris verifies the published execution.
Piero independently checks reproduction and reported results.

1. Publish an early working version on Qollab if required.
2. Verify the required simulator paths.
3. Complete the project page and run instructions.
4. Include MIT licensing, source attribution, and required acknowledgments.
5. Explain the original contribution and scientific limitations.
6. Produce the public 2-3 minute demonstration video if required.
7. Check all submission links and access requirements.
8. Submit through the team page before the deadline in `context.md`.
9. Verify the submission confirmation.

GitHub publication alone is not the hackathon submission.

## Handoff format

For each completed task, report:

- Completed behavior.
- Changed files and branch or pull-request link.
- How another teammate runs or uses it.
- Checks actually performed.
- Remaining limitations and next owner.

Update shared contracts through team coordination. Do not silently change inputs or outputs.

