import argparse
import logging
from typing import Union

from MoleculaPy.molecule_utils import Molecule
from pathlib import Path
import time
import os.path

LOG_DIR_PATH = Path(f"{os.path.dirname(os.path.abspath(__file__))}/logs")
LOG_FILE_PATH = Path(f"{time.strftime('%Y%m%d-%H%M%S')}.log")
LOG_FULL_PATH = LOG_DIR_PATH.joinpath(LOG_FILE_PATH)


def setup_logging():
    """
    Set up logging configuration for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler(LOG_FULL_PATH)
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
