import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog='MoleculaPy',
        description='Calculate molecular descriptors or fingerprints for molecules provided in a file.',
        epilog='Thanks for using %(prog)\'s! :)'
    )

    parser.add_argument('input_file', help='Path to the input file', type=str)
    parser.add_argument('output_file', help='Path to the output file', type=str)
    parser.add_argument('--method',
                        choices=['descriptors', 'fingerprints'],
                        default='descriptors',
                        help='(Optional) Calculation method: descriptors or fingeprints',
                        type=str)
    parser.add_argument('--fp_type',
                        choices=['Atom', 'MACCS', 'Morgan', 'Topological', 'RDKit'],
                        default='Morgan',
                        help='(Optional) Fingerprint type',
                        type=str)
    parser.add_argument('--remove_salt',
                        action=argparse.BooleanOptionalAction,
                        default=True,
                        help='(Optional) Remove salts from SMILE.',
                        type=bool)
    parser.add_argument('--n_bits',
                        default=2048,
                        help='(Optional) Number of bits of a given fingerprints type.',
                        type=int)

    args = parser.parse_args()
    return args
