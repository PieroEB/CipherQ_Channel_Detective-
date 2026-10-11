import unittest

from src.channel_detective.evidence_lab import (
    EvidenceCase,
    build_evidence_report,
    format_report_table,
    sample_size_sweep,
)
from src.channel_detective.bb84_simulator import simulate_bb84


class BB84SimulatorTests(unittest.TestCase):
    def test_ideal_channel_has_low_error_with_seeded_run(self):
        result = simulate_bb84(
            scenario="ideal",
            transmitted=2000,
            public_sample_size=300,
            seed=42,
        )

        self.assertEqual(result.errors, 0)
        self.assertEqual(result.qber, 0)

    def test_intercept_resend_introduces_disturbance(self):
        result = simulate_bb84(
            scenario="intercept",
            transmitted=4000,
            public_sample_size=800,
            eve_intercept_probability=1.0,
            seed=42,
        )

        self.assertGreater(result.qber, 0.15)
        self.assertLess(result.qber, 0.35)

    def test_noise_can_produce_errors_without_eve(self):
        result = simulate_bb84(
            scenario="noise",
            transmitted=3000,
            public_sample_size=500,
            noise_probability=0.08,
            seed=7,
        )

        self.assertGreater(result.errors, 0)
        self.assertEqual(result.scenario, "noise")


class EvidenceLabTests(unittest.TestCase):
    def test_sweep_reports_uncertainty_for_each_sample_size(self):
        reports = sample_size_sweep(
            scenario="intercept",
            transmitted=2500,
            sample_sizes=(20, 100, 400),
            seed=3,
        )

        self.assertEqual(len(reports), 3)
        self.assertEqual([report.result.sample_size for report in reports], [20, 100, 400])
        self.assertGreater(reports[0].uncertainty_width, reports[-1].uncertainty_width)

    def test_evidence_report_formats_percentages(self):
        report = build_evidence_report(
            case=EvidenceCase(
                label="format check",
                scenario="noise",
                transmitted=1000,
                public_sample_size=100,
                noise_probability=0.12,
                seed=5,
            )
        )
        table = format_report_table([report])

        self.assertIn("format check", table)
        self.assertIn("%", table)
        self.assertIn("conclusion", table)


if __name__ == "__main__":
    unittest.main()
