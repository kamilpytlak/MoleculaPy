import argparse
import unittest
from unittest.mock import patch

from MoleculaPy.cli import _parse_args


class TestParser(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(input_file='input.txt',
                                           output_file='output.txt',
                                           method='descriptors',
                                           fp_type='Morgan',
                                           remove_salt=True))
    def test_default_args(self, *args):
        args = _parse_args()
        self.assertEqual(args.method, 'descriptors')
        self.assertEqual(args.fp_type, 'Morgan')
        self.assertTrue(args.remove_salt)


if __name__ == '__main__':
    unittest.main()
