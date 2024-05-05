import logging
from typing import Dict

from rdkit.Chem import MolFromSmiles, MolToSmiles, SaltRemover, AllChem, MACCSkeys, RDKFingerprint
from rdkit.Chem.Descriptors import CalcMolDescriptors


class Molecule:
    def __init__(self, smiles: str):
        """
        Initializes a Molecule object with the provided SMILES notation.

        Parameters
        ----------
        smiles : str
            The SMILES notation for the molecule.

        Raises
        ------
        ValueError
            If an empty SMILES string or an invalid SMILES string is provided.
        """
        self.logger = logging.getLogger(__name__)

        if not smiles:
            self.logger.warning('Empty SMILES string provided.')
            raise ValueError('Empty SMILES string provided.')

        self.smiles = smiles
        self.cleaned_smiles = None
        self.mol = MolFromSmiles(smiles)

        if self.mol is None:
            self.logger.warning(f"Invalid SMILES string provided: {self.smiles}")
            raise ValueError('Invalid SMILES string provided.')

    def remove_salt(self):
        """
        Remove salt from the molecule's SMILES notation and updates the cleaned_smiles attribute.
        """
        remover = SaltRemover.SaltRemover()
        self.mol = remover.StripMol(self.mol, dontRemoveEverything=True, sanitize=True)
        self.cleaned_smiles = MolToSmiles(self.mol)

    def calculate_descriptors(self) -> Dict[str, float]:
        """
        Calculate molecular descriptor using RDKit.

        Returns
        -------
        desc_dict : dict
            A dictionary containing molecular descriptors and their corresponding values.
        """
        desc_dict = CalcMolDescriptors(self.mol)
        self.logger.info(f"Calculated descriptors for SMILES: {self.smiles}")
        return desc_dict

    def calculate_fingerprints(self, fp_type: str, n_bits: int = 2048) -> Dict[str, bool]:
        fp_method = {
            'Atom': AllChem.GetHashedAtomPairFingerprintAsBitVect,
            'MACCS': MACCSkeys.GenMACCSKeys,
            'Morgan': AllChem.GetMorganFingerprintAsBitVect,
            'RDKit': RDKFingerprint,
            'Topological': AllChem.GetHashedTopologicalTorsionFingerprintAsBitVect
        }

        if fp_type not in fp_method:
            raise ValueError(f"Unknown fingerprint type {fp_type}.")

        if n_bits < 1:
            raise ValueError(f"n_bits cannot be less than 1 (n_bits: {n_bits}).")

        fp_func = fp_method[fp_type]
        if fp_type == 'Morgan':
            fp = fp_func(self.mol, 2, nBits=n_bits)
        elif fp_type == 'MACCS':
            fp = fp_func(self.mol)
        else:
            fp = fp_func(self.mol, nBits=n_bits)

        fp_list = fp.ToList()
        fp_dict = {f"{fp_type}_{i}": int(bit) for i, bit in enumerate(fp_list)}
        self.logger.info(f"Calculated fingerprint for SMILES {self.smiles}.")

        return fp_dict


smiles = "COC1=C(C=C2C(=C1)CC(C2=O)CC3CCN(CC3)CC4=CC=CC=C4)OC"
ex_molecule = Molecule(smiles)
ex_molecule.remove_salt()

print(ex_molecule.calculate_descriptors())
