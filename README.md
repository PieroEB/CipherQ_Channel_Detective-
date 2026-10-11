# CipherQ Channel Detective

Educational quantum-security lab for investigating what BB84 error rates can and cannot justify.

The project simulates three scenarios:

- Ideal communication.
- Intercept-resend attack by Eve.
- Channel/equipment perturbation without an attacker.

The goal is not to build a real secure messaging product. The goal is to help a user distinguish observation, hypothesis, and justified conclusion when quantum-key-distribution data is noisy or statistically weak.

## Core Question

> What do these errors allow us to claim?

The lab shows a BB84 exchange, keeps only matching-basis bits, samples part of the sifted key, and reports:

- Observed quantum bit error rate (QBER).
- Confidence interval for uncertainty.
- A cautious evidence label.
- Scenario comparison notes.

## Suggested Demo Flow

1. Start with an unknown scenario.
2. Run a small sample and show that uncertainty is high.
3. Increase sample size and compare how the evidence changes.
4. Reveal whether the run was ideal, intercept-resend, or noisy.
5. Explain why errors alone do not prove an attacker.

## Team Split

See [docs/team_roles.md](docs/team_roles.md) for the role split based on the three resumes.

## Project Structure

```text
docs/
  project_plan.md       High-level build plan and judging narrative.
  team_roles.md         Ownership split for Piero, Boris, and Adrian.
src/channel_detective/
  bb84_simulator.py     Initial BB84 simulation and statistics engine.
tests/
  test_bb84_simulator.py
```

## Quick Start

Run the simulator:

```bash
python3 src/channel_detective/bb84_simulator.py --scenario intercept --n 2000 --sample 300 --seed 7
```

Run tests:

```bash
python3 -m unittest discover -s tests
```

Run Piero's evidence demo:

```bash
python3 -m src.channel_detective.evidence_lab --mode demo
```

Compare how uncertainty changes with public sample size:

```bash
python3 -m src.channel_detective.evidence_lab --mode sweep --scenario intercept
```

## Next Build Step

Use the simulator as the backend logic, then add either:

- A FastAPI endpoint for `/simulate`.
- A React interface with controls for scenario, sample size, and perturbation.
