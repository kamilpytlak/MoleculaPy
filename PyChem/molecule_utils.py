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
        if not smiles:
            raise ValueError('Empty SMILES string provided.')

        self.smiles = smiles
        self.cleaned_smiles = None
        self.mol = MolFromSmiles(smiles)

        if self.mol is None:
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
        return desc_dict

    def calculate_fingerprints(self, fp_type: str, nBits: 2048) -> Dict[str, bool]:
        fp_method = {
            'Atom': AllChem.GetHashedAtomPairFingerprintAsBitVect,
            'MACCS': MACCSkeys.GenMACCSKeys,
            'Morgan': AllChem.GetMorganFingerprintAsBitVect,
            'RDKit': RDKFingerprint,
            'Topological': AllChem.GetHashedTopologicalTorsionFingerprintAsBitVect
        }

        if fp_type not in fp_method:
            raise ValueError(f"Unknown fingerprint type {fp_type}.")

        fp_func = fp_method[fp_type]
        fp = fp_func(self.mol, nBits=nBits) if fp_type != 'MACCS' else fp_func(self.mol)

        fp_list = fp.ToList()
        fp_dict = {f"{fp_type}_{i}": bit for i, bit in enumerate(fp_list)}

        return fp_dict
