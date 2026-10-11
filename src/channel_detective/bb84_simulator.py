from __future__ import annotations

import argparse
import math
import random
from dataclasses import asdict, dataclass
from typing import Literal


Basis = Literal["Z", "X"]
Scenario = Literal["ideal", "intercept", "noise"]


@dataclass(frozen=True)
class SimulationResult:
    scenario: Scenario
    transmitted: int
    sifted: int
    sample_size: int
    errors: int
    qber: float
    ci_low: float
    ci_high: float
    conclusion: str


def _rand_basis(rng: random.Random) -> Basis:
    return "Z" if rng.random() < 0.5 else "X"


def _measure_prepared_bit(
    prepared_bit: int,
    prepared_basis: Basis,
    measurement_basis: Basis,
    rng: random.Random,
) -> int:
    if prepared_basis == measurement_basis:
        return prepared_bit
    return 1 if rng.random() < 0.5 else 0


def _wilson_interval(errors: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total == 0:
        return 0.0, 1.0

    phat = errors / total
    denominator = 1 + z * z / total
    center = (phat + z * z / (2 * total)) / denominator
    margin = z * math.sqrt((phat * (1 - phat) + z * z / (4 * total)) / total) / denominator
    return max(0.0, center - margin), min(1.0, center + margin)


def _conclusion(sample_size: int, qber: float, ci_low: float, ci_high: float) -> str:
    if sample_size < 50:
        return "Data insufficient: the public sample is too small for a confident claim."
    if ci_high < 0.08:
        return "No strong perturbation signal in this sample."
    if ci_low <= 0.12 <= ci_high:
        return "Ambiguous: compatible with noise or attack-like disturbance."
    if qber >= 0.18 and ci_low > 0.10:
        return "Strong evidence of perturbation, but the cause is not identified by errors alone."
    return "Some evidence of disturbance; collect more data or compare against a channel-noise model."


def simulate_bb84(
    *,
    scenario: Scenario,
    transmitted: int = 1000,
    public_sample_size: int = 100,
    noise_probability: float = 0.02,
    eve_intercept_probability: float = 1.0,
    seed: int | None = None,
) -> SimulationResult:
    if transmitted <= 0:
        raise ValueError("transmitted must be positive")
    if public_sample_size <= 0:
        raise ValueError("public_sample_size must be positive")
    if not 0 <= noise_probability <= 1:
        raise ValueError("noise_probability must be between 0 and 1")
    if not 0 <= eve_intercept_probability <= 1:
        raise ValueError("eve_intercept_probability must be between 0 and 1")

    rng = random.Random(seed)
    sifted_pairs: list[tuple[int, int]] = []

    for _ in range(transmitted):
        alice_bit = 1 if rng.random() < 0.5 else 0
        alice_basis = _rand_basis(rng)
        bob_basis = _rand_basis(rng)

        sent_bit = alice_bit
        sent_basis = alice_basis

        if scenario == "intercept" and rng.random() < eve_intercept_probability:
            eve_basis = _rand_basis(rng)
            sent_bit = _measure_prepared_bit(alice_bit, alice_basis, eve_basis, rng)
            sent_basis = eve_basis

        bob_bit = _measure_prepared_bit(sent_bit, sent_basis, bob_basis, rng)

        if scenario == "noise" and rng.random() < noise_probability:
            bob_bit = 1 - bob_bit

        if alice_basis == bob_basis:
            sifted_pairs.append((alice_bit, bob_bit))

    sample_size = min(public_sample_size, len(sifted_pairs))
    sample = rng.sample(sifted_pairs, sample_size) if sample_size else []
    errors = sum(1 for alice_bit, bob_bit in sample if alice_bit != bob_bit)
    qber = errors / sample_size if sample_size else 0.0
    ci_low, ci_high = _wilson_interval(errors, sample_size)

    return SimulationResult(
        scenario=scenario,
        transmitted=transmitted,
        sifted=len(sifted_pairs),
        sample_size=sample_size,
        errors=errors,
        qber=qber,
        ci_low=ci_low,
        ci_high=ci_high,
        conclusion=_conclusion(sample_size, qber, ci_low, ci_high),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate BB84 channel evidence.")
    parser.add_argument("--scenario", choices=["ideal", "intercept", "noise"], required=True)
    parser.add_argument("--n", type=int, default=1000, help="Transmitted qubits")
    parser.add_argument("--sample", type=int, default=100, help="Public comparison sample size")
    parser.add_argument("--noise", type=float, default=0.02, help="Noise probability for noise scenario")
    parser.add_argument("--eve", type=float, default=1.0, help="Eve intercept probability")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    result = simulate_bb84(
        scenario=args.scenario,
        transmitted=args.n,
        public_sample_size=args.sample,
        noise_probability=args.noise,
        eve_intercept_probability=args.eve,
        seed=args.seed,
    )
    for key, value in asdict(result).items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

