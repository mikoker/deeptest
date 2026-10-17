import unittest

from deeptesting.cli import _parser


class CliTests(unittest.TestCase):
    def test_latest_deeptesting_app_version_is_default(self):
        args = _parser().parse_args(["unlock-condition-match"])
        self.assertEqual(args.app_version, 17000004)


if __name__ == "__main__":
    unittest.main()
