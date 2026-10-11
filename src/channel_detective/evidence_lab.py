from __future__ import annotations

import argparse
from dataclasses import dataclass

from .bb84_simulator import Scenario, SimulationResult, simulate_bb84


@dataclass(frozen=True)
class EvidenceCase:
    label: str
    scenario: Scenario
    transmitted: int
    public_sample_size: int
    noise_probability: float = 0.02
    eve_intercept_probability: float = 1.0
    seed: int | None = None


@dataclass(frozen=True)
class EvidenceReport:
    label: str
    result: SimulationResult
    uncertainty_width: float
    qber_percent: float
    ci_low_percent: float
    ci_high_percent: float


DEFAULT_DEMO_CASES: tuple[EvidenceCase, ...] = (
    EvidenceCase(
        label="Tiny public sample, intercept-resend",
        scenario="intercept",
        transmitted=600,
        public_sample_size=24,
        eve_intercept_probability=1.0,
        seed=11,
    ),
    EvidenceCase(
        label="Larger public sample, intercept-resend",
        scenario="intercept",
        transmitted=4000,
        public_sample_size=800,
        eve_intercept_probability=1.0,
        seed=11,
    ),
    EvidenceCase(
        label="Noise-only channel that can look suspicious",
        scenario="noise",
        transmitted=4000,
        public_sample_size=800,
        noise_probability=0.20,
        seed=17,
    ),
    EvidenceCase(
        label="Ideal channel baseline",
        scenario="ideal",
        transmitted=2000,
        public_sample_size=300,
        seed=23,
    ),
)


def build_evidence_report(case: EvidenceCase) -> EvidenceReport:
    result = simulate_bb84(
        scenario=case.scenario,
        transmitted=case.transmitted,
        public_sample_size=case.public_sample_size,
        noise_probability=case.noise_probability,
        eve_intercept_probability=case.eve_intercept_probability,
        seed=case.seed,
    )
    return EvidenceReport(
        label=case.label,
        result=result,
        uncertainty_width=result.ci_high - result.ci_low,
        qber_percent=result.qber * 100,
        ci_low_percent=result.ci_low * 100,
        ci_high_percent=result.ci_high * 100,
    )


def sample_size_sweep(
    *,
    scenario: Scenario,
    transmitted: int = 5000,
    sample_sizes: tuple[int, ...] = (20, 50, 100, 250, 500, 1000),
    noise_probability: float = 0.02,
    eve_intercept_probability: float = 1.0,
    seed: int = 7,
) -> list[EvidenceReport]:
    reports: list[EvidenceReport] = []

    for index, sample_size in enumerate(sample_sizes):
        case = EvidenceCase(
            label=f"{scenario} sample={sample_size}",
            scenario=scenario,
            transmitted=transmitted,
            public_sample_size=sample_size,
            noise_probability=noise_probability,
            eve_intercept_probability=eve_intercept_probability,
            seed=seed + index,
        )
        reports.append(build_evidence_report(case))

    return reports


def format_report_table(reports: list[EvidenceReport]) -> str:
    headers = (
        "case",
        "scenario",
        "sample",
        "errors",
        "qber",
        "95% ci",
        "ci width",
        "conclusion",
    )
    rows = [
        (
            report.label,
            report.result.scenario,
            str(report.result.sample_size),
            str(report.result.errors),
            f"{report.qber_percent:.1f}%",
            f"{report.ci_low_percent:.1f}% - {report.ci_high_percent:.1f}%",
            f"{report.uncertainty_width * 100:.1f} pp",
            report.result.conclusion,
        )
        for report in reports
    ]

    widths = [
        max(len(str(row[column])) for row in (headers, *rows))
        for column in range(len(headers))
    ]

    def format_row(row: tuple[str, ...]) -> str:
        return " | ".join(value.ljust(widths[index]) for index, value in enumerate(row))

    separator = "-+-".join("-" * width for width in widths)
    return "\n".join([format_row(headers), separator, *(format_row(row) for row in rows)])


def demo_reports() -> list[EvidenceReport]:
    return [build_evidence_report(case) for case in DEFAULT_DEMO_CASES]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Channel Detective evidence demos.")
    parser.add_argument(
        "--mode",
        choices=["demo", "sweep"],
        default="demo",
        help="demo compares prepared judge cases; sweep shows sample-size uncertainty.",
    )
    parser.add_argument("--scenario", choices=["ideal", "intercept", "noise"], default="intercept")
    parser.add_argument("--noise", type=float, default=0.02)
    parser.add_argument("--eve", type=float, default=1.0)
    args = parser.parse_args()

    if args.mode == "demo":
        reports = demo_reports()
    else:
        reports = sample_size_sweep(
            scenario=args.scenario,
            noise_probability=args.noise,
            eve_intercept_probability=args.eve,
        )

    print(format_report_table(reports))


if __name__ == "__main__":
    main()

