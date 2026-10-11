# Channel Detective - Project Context

## Status

Channel Detective is a new project by team CipherQ for the Qollab x IonQ Global Quantum Hackathon.

The team has created and cloned its GitHub repository. The initial repository foundation, simulator module, documentation, and tests are being established.

Plans in this document are not claims of completed functionality unless the relevant code and checks are present in the repository.

## Purpose

Build an educational quantum-communication lab where a user investigates BB84 exchange data and decides what the observed errors justify.

The project should teach that:

- Quantum measurement basis choices matter.
- Intercept-resend attacks can introduce disturbance.
- Benign channel/equipment noise can also introduce errors.
- Small samples can mislead.
- Error rates support hypotheses but do not automatically identify an attacker.

Primary theme: Quantum Unlocked.

## Minimum working experience

A user can:

1. Select or receive a hidden scenario.
2. Choose transmitted qubit count and public sample size.
3. Run a BB84 simulation.
4. Inspect sifted-key size, public-sample size, errors, QBER, and uncertainty.
5. Compare ideal, intercept-resend, and noise-only scenarios.
6. Reveal the scenario and understand what could and could not be concluded.

Initial scope: BB84, one intercept-resend model, one simple perturbation/noise model, and statistical analysis of public-sample errors.

## Initial scenarios

### Ideal

Alice prepares random bits in random bases. Bob measures in random bases. After sifting, matching-basis bits agree except for simulator implementation limits.

### Intercept-resend

Eve intercepts with a configurable probability, chooses a random basis, measures, and resends the measured state. When Eve's basis differs from Alice's, she can disturb Bob's matching-basis result.

### Noise only

No Eve is present. Bob's outcome can be flipped with a configurable perturbation probability, representing channel or device disturbance.

## Team ownership

- Adrian: BB84 protocol accuracy, Qiskit path, intercept-resend model, quantum/security explanation, and limitation language.
- Boris: FastAPI or app integration, response schemas, tests, dependency handling, and deployment packaging.
- Piero: statistical evidence panel, uncertainty visualization, demo storyline, analysis of false alarms and sample-size effects.

Ownership is flexible. Coordinate overlapping edits and shared-interface changes.

Every teammate must understand the complete demonstration.

## Architecture

One simulation request feeds three layers:

- Quantum/protocol layer: prepare, measure, optionally intercept, optionally perturb.
- Classical processing layer: sift matching bases, sample public bits, calculate errors.
- Evidence layer: calculate QBER, confidence interval, and cautious interpretation.

If a web app is built, the simulation contract should support:

- Scenario.
- Transmitted qubits.
- Public sample size.
- Noise probability.
- Eve intercept probability.
- Random seed.
- Revealed or hidden scenario mode.

## Scientific boundaries

- QBER is an observed statistic, not a cause label.
- Intercept-resend and noise can produce similar error rates.
- Small public samples can produce false alarms or false reassurance.
- A simulation is an educational model, not a deployable QKD system.
- A "no attack detected" message is not a security proof.
- Confidence intervals must be shown or explained when interpreting sampled data.
- Any Qiskit circuit construction must match the stated BB84 model.
- Random seeds and fixed demo cases should be labeled when used.

## Hackathon requirements

Based on the team plan and organizer context:

- Build the submitted contribution within the official hackathon window.
- Use Qiskit for the quantum component.
- Publish a public, runnable Qollab project under the MIT license.
- Verify execution on the required Qollab simulator path if Qollab submission is required.
- Provide a project page explaining purpose, method, execution, results, and limitations.
- Follow UI accessibility best practices.
- Include a public 2-3 minute demonstration video if required.
- Attribute reused libraries, templates, code, explanations, and AI assistance.
- Include: "This effort is supported by Qollab & IonQ" if required by the organizers.
- The captain submits through the team page.
- Submission deadline: October 11, 2026, at 7:00 p.m. Eastern Time.

GitHub is the development repository. It does not replace Qollab publication or the submission action.

## Platform constraints requiring verification

Boris and Adrian should verify:

- Available Python and Qiskit versions.
- Whether Qollab supports the chosen UI format.
- Whether external Python packages beyond Qiskit are allowed.
- Backend shot limits and circuit limits.
- Whether IonQ execution permits one circuit per job.
- How project publication and updates work.

Do not assume React, Streamlit, a separate server, or arbitrary packages are supported until verified.

## Scope control

Prioritize one working end-to-end lab path, then expand.

Initially exclude:

- A real secure chat.
- Full production QKD.
- Authentication systems.
- Cryptographic key management beyond educational BB84 sampling.
- Claims of guaranteed attack attribution.
- Paid APIs or private credentials.

## Keeping context current

Record consequential team decisions here and technical contracts in a dedicated interface document when needed.

Distinguish planned, implemented, and verified behavior.

When a newer organizer announcement changes a requirement, record the update and its source before relying on it.

