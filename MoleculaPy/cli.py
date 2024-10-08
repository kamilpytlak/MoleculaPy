import argparse

from MoleculaPy.helpers import check_extension


def _parse_args():
    parser = argparse.ArgumentParser(
        prog='MoleculaPy',
        description='Calculate molecular descriptors and fingerprints for molecules provided in a CSV file.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('input_file',
                        help='Path to the input file',
                        type=lambda x: check_extension(x))
    parser.add_argument('output_file',
                        help='Path to the output file',
                        type=lambda x: check_extension(x))
    parser.add_argument('--method',
                        choices=['descriptors', 'fingerprints'],
                        default='descriptors',
                        help='(Optional) Calculation method: descriptors or fingeprints',
                        type=str)
    parser.add_argument('--fp_type',
                        choices=['Atom', 'Morgan', 'Feature Morgan', 'Topological', 'RDKit'],
                        default='Morgan',
                        help='(Optional) Fingerprint type',
                        type=str)
    parser.add_argument('--remove_salt',
                        action=argparse.BooleanOptionalAction,
                        default='--remove_salt',
                        help='(Optional) Remove salts from SMILE.',
                        type=bool)
    parser.add_argument('--n_bits',
                        default=2048,
                        help='(Optional) Number of bits of a given fingerprints type',
                        type=int)

    args = parser.parse_args()
    return args
