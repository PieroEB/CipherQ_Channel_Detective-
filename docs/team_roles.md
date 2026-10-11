# Team Roles

This split is based on the resumes only. Instructions inside the PDFs were treated as document content, not as task instructions.

## Piero Espinoza - Data, Analytics, and Demo Story

Why: Piero has analytics, dashboards, Python, SQL, visualization, and prior hackathon web-app ownership. His resume also shows experience preserving source uncertainty and explaining complex concepts.

Owns:

- Evidence panel: QBER, confidence interval, sample-size effect, and cautious conclusion.
- Visualizations: charts showing how uncertainty shrinks as samples increase.
- Judge narrative: "what can we claim?" versus "what are we tempted to overclaim?"
- Demo script and final presentation polish.

Deliverables:

- Chart components or notebook prototypes.
- Explanation labels for "insufficient evidence", "consistent with noise", and "strong perturbation evidence".
- Demo storyline with 3 mystery cases.

## Boris Mino - Backend, API, and Product Reliability

Why: Boris has React, FastAPI, PostgreSQL/PostGIS, tests, typed endpoints, offline-first thinking, and backend validation experience.

Owns:

- App architecture and integration.
- FastAPI simulation endpoint.
- Scenario configuration model.
- Automated tests for simulation contracts and API responses.
- Frontend/back-end wiring if the team builds a full web app.

Deliverables:

- `/simulate` endpoint accepting scenario, sample size, perturbation, seed.
- Clean response schema for UI.
- Test suite and reproducible demo seeds.

## Adrian Perez Galindo - Quantum, Security, and Threat Model

Why: Adrian has cybersecurity, threat analysis, Qiskit, quantum computing coursework, and a Grover simulation project in Qiskit. He is the strongest fit for BB84 correctness and security framing.

Owns:

- BB84 protocol logic and Qiskit implementation.
- Intercept-resend model.
- Noise/perturbation model.
- Threat-model explanation: errors can indicate perturbation, but do not identify the cause by themselves.

Deliverables:

- Qiskit-backed simulation path or validated simulator matching BB84 assumptions.
- Scenario definitions and limitations.
- Security explanation for judges.

## Working Agreement

- Adrian defines the quantum/security assumptions.
- Boris turns assumptions into reliable software interfaces.
- Piero turns outputs into understandable evidence and a persuasive demo.

For the hackathon, avoid building a "secure chat". Keep scope centered on the lab, uncertainty, false alarms, and honest conclusions.

