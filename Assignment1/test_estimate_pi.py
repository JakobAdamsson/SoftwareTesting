import unittest
from estimate_pi import estimate_pi, PiFileWriter
from unittest.mock import patch
from pathlib import Path


class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self) -> None:
        """A method that checks the estimate_pi function with a large value"""
        pi_expected: int = 3.141592653589793
        pi_actual: int = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01)

    def test_estimate_pi_medium_value(self) -> None:
        """A method that checks the estimate_pi function with a medium value"""
        pi_expected: int = 3.141592653589793
        estimated_pi_value: int = estimate_pi(10000)
        self.assertAlmostEqual(pi_expected, estimated_pi_value, delta=0.05)

    def test_estimate_pi_small_n(self) -> None:
        """A method that checks the estimate_pi function with a small value"""
        estimated_pi_value: int = estimate_pi(1)
        self.assertTrue(estimated_pi_value in [0, 4])

    def test_estimate_pi_gt_one(self) -> None:
        """
        A method that tests if the estimate_pi function returns 4 when the value is greater than 1.
        Meaning count will be incremebted -> 4*1/1 = 4
        """
        with patch("random.uniform", return_value=0.5):
            estimated_pi_value: int = estimate_pi(1)
            self.assertEqual(estimated_pi_value, 4)

    def test_estimate_pi_loe_to_one(self) -> None:
        """
        A method that tests if the estimate_pi function returns 0 when the value is less than, or equal to 1.
        Meaning count will never be incremebted -> 4*0/1 = 0
        """
        with patch("random.uniform", return_value=1):
            estimated_pi_value: int = estimate_pi(1)
            self.assertEqual(estimated_pi_value, 0)


class TestPiWriter(unittest.TestCase):
    def test_file_writer(self) -> None:
        """A method that mocks a file writer, meaning we simulate a file being opened and written to"""
        filepath: Path = Path("fake/file/path")
        content: str = "1234"
        with unittest.mock.patch(
            "__main__.__builtins__.open", unittest.mock.mock_open()
        ) as mocked_file:
            PiFileWriter().write(content, filepath)
            mocked_file.assert_called_once_with(filepath, "w", encoding="utf8")
            mocked_file().write.assert_called_once_with(content)


if __name__ == "__main__":
    unittest.main()
