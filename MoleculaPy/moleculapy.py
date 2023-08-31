import logging
import os
import os.path
import sys
import time

from MoleculaPy.cli import parse_args
from MoleculaPy.helpers import convert_to_molecule

import pandas as pd
from tqdm import tqdm


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler(f"{os.getcwd()}/logs/{time.strftime('%Y%m%d-%H%M%S')}")
        ]
    )

    args = parse_args()

    if not os.path.exists(args.input_file):
        print(f"The path {args.input_file} is not specified in your system.")
        sys.exit()

    smiles_df = pd.read_csv(args.input_file)
    smiles_df.rename(columns=lambda x: x.title(), inplace=True)

    tqdm.pandas(desc='Converting SMILES to mol objects...')
    moles = smiles_df['Smiles'].progress_apply(convert_to_molecule).dropna()

    if args.remove_salt:
        tqdm.pandas(desc='Removing salts...')
        moles.progress_apply(lambda mol: mol.remove_salt())

    if args.method == 'descriptors':
        tqdm.pandas(desc='Calculating descriptors...')
        descriptors_df = moles.progress_apply(lambda mol: mol.calculate_descriptors())
        descriptors_df = pd.DataFrame(descriptors_df.to_list(), index=descriptors_df.index)

        final_df = pd.merge(smiles_df, descriptors_df, how='left', left_index=True, right_index=True)
        final_df.to_csv(args.output_file, index=False)

    elif args.method == 'fingerprints':
        tqdm.pandas(desc=f"Calculating {args.fp_type} fingerprints...")
        fingerprints_df = moles.progress_apply(lambda mol: mol.calculate_fingerprints(args.fp_type, args.n_bits))
        fingerprints_df = pd.DataFrame(fingerprints_df.to_list(), index=fingerprints_df.index)

        final_df = pd.merge(smiles_df, fingerprints_df, how='left', left_index=True, right_index=True)
        final_df.to_csv(args.output_file, index=False)


if __name__ == '__main__':
    main()
