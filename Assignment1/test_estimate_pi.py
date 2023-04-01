import unittest
from estimate_pi import estimate_pi, PiFileWriter
from unittest.mock import MagicMock, mock_open, patch
from pathlib import Path


class TestEstimatePi(unittest.TestCase):
    def test_estimate_pi(self):
        pi_expected = 3.141592653589793
        pi_actual = estimate_pi(1000000)
        self.assertAlmostEqual(pi_expected, pi_actual, delta=0.01)

    def test_estimate_pi_valid_input(self):
        pi_expected = 3.141592653589793
        self.assertIsInstance(pi, int, "pi is not an integer")


class TestPiWriter(unittest.TestCase):
    def test_file_writer(self):
        fake_file_path = "fake/file/path"
        content = "1234"
        with unittest.mock.patch(
            "__main__.__builtins__.open", unittest.mock.mock_open()
        ) as mocked_file:
            PiFileWriter().write(content, fake_file_path)
            mocked_file.assert_called_once_with(fake_file_path, "w", encoding="utf8")
            mocked_file().write.assert_called_once_with(content)

    def test_file_writer_valid_args(self):
        content: str = "3.1415"
        filepath: Path = Path("fake/file/path")
        self.assertIsInstance(content, str)
        self.assertIsInstance(filepath, Path)

        _mock = mock_open()

        # Mock a file open
        with patch("builtins.open", _mock) as mocked_file:
            PiFileWriter().write(content, filepath)

        mocked_file.assert_called_once_with(filepath, "w", encoding="utf8")

        # Mock a file write
        _mock().write.assert_called_once_with(content)

    def test_file_writer_empty_content(self):
        content = ""
        filepath = "fake/file/path"

        _mock = mock_open()
        with patch("builtins.open", _mock) as mocked_file:
            PiFileWriter().write(content, filepath)

        mocked_file.assert_called_once_with(filepath, "w", encoding="utf8")

        # Mock a file write
        _mock().write.assert_called_once_with(content)


if __name__ == "__main__":
    unittest.main()
