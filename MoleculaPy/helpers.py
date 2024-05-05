import argparse
import logging
import os.path
import time
from typing import Union

from MoleculaPy.molecule_utils import Molecule


def setup_logging(log_dir_path: str):
    """
    Set up logging configuration for the application.
    """
    log_save_path = os.path.join(log_dir_path, f"{time.strftime('%Y%m%d-%H%M%S')}.log")
    logging.basicConfig(
        encoding="utf-8",
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler(log_save_path)
        ]
    )


def check_extension(filepath: str, extensions: tuple = 'csv') -> Union[argparse.ArgumentTypeError, str]:
    if not filepath.endswith(extensions):
        raise argparse.ArgumentTypeError('Not a valid filename extension.')
    return filepath


def check_n_bits(n_bits: int) -> Union[argparse.ArgumentTypeError, int]:
    if n_bits < 1:
        raise argparse.ArgumentTypeError('n_bits cannot be less than 1.')
    return n_bits


def convert_to_molecule(smiles: str):
    try:
        return Molecule(smiles)
    except ValueError:
        return None
