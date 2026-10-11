import unittest

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


if __name__ == "__main__":
    unittest.main()

