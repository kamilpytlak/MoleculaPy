import unittest

from rdkit.Chem import MolToSmiles

from MoleculaPy.molecule_utils import Molecule


class TestMolecule(unittest.TestCase):
    def test_valid_smiles(self):
        valid_smiles = 'CC=O'
        mol = Molecule(valid_smiles)
        self.assertEqual(mol.smiles, valid_smiles)

    def test_empty_smiles(self):
        empty_smiles = ''
        with self.assertRaises(ValueError):
            Molecule(empty_smiles)

    def test_invalid_smiles(self):
        invalid_smiles = 'ThisSmilesIsInvalid'
        with self.assertRaises(ValueError):
            Molecule(invalid_smiles)

    def test_remove_salt_with_salt(self):
        valid_smiles_with_salt = 'CCO.[Na+]'
        valid_smiles_without_salt = 'CCO'

        mol = Molecule(valid_smiles_with_salt)
        mol.remove_salt()
        self.assertEqual(mol.cleaned_smiles, valid_smiles_without_salt)

    def test_remove_salt_no_salt(self):
        valid_smiles_without_salt = 'CCCCCCCCCCCCCCCCC(=O)O'

        mol = Molecule(valid_smiles_without_salt)
        mol.remove_salt()
        self.assertEqual(mol.cleaned_smiles, valid_smiles_without_salt)

    def test_calculate_descriptors(self):
        valid_smiles = 'COC1=C(C=C2C(=C1)CC(C2=O)CC3CCN(CC3)CC4=CC=CC=C4)OC'
        mol = Molecule(valid_smiles)
        mol.remove_salt()
        expected_descriptors = dict(MaxAbsEStateIndex=12.936933437749705, MaxEStateIndex=12.936933437749705,
                                    MinAbsEStateIndex=0.10878294861970894, MinEStateIndex=0.10878294861970894,
                                    qed=0.747461491562485, MolWt=379.50000000000006, HeavyAtomMolWt=350.26800000000014,
                                    ExactMolWt=379.214743788, NumValenceElectrons=148, NumRadicalElectrons=0,
                                    MaxPartialCharge=0.16620209627378937, MinPartialCharge=-0.49285879087511075,
                                    MaxAbsPartialCharge=0.49285879087511075, MinAbsPartialCharge=0.16620209627378937,
                                    FpDensityMorgan1=1.0, FpDensityMorgan2=1.6785714285714286,
                                    FpDensityMorgan3=2.357142857142857, BCUT2D_MWHI=16.507852598036713,
                                    BCUT2D_MWLOW=9.851170413196193, BCUT2D_CHGHI=2.340516458126292,
                                    BCUT2D_CHGLO=-2.3249762834480796, BCUT2D_LOGPHI=2.391365158467486,
                                    BCUT2D_LOGPLOW=-2.3381059044692702, BCUT2D_MRHI=6.024698499182426,
                                    BCUT2D_MRLOW=0.08952545146688057, AvgIpc=3.033559459933484,
                                    BalabanJ=1.3362548695620298, BertzCT=825.2439471833665, Chi0=19.509860921691395,
                                    Chi0n=16.817858357904015, Chi0v=16.817858357904015, Chi1=13.67336639324559,
                                    Chi1n=10.229959823676923, Chi1v=10.229959823676923, Chi2n=8.070461212884847,
                                    Chi2v=8.070461212884847, Chi3n=6.285957345712203, Chi3v=6.285957345712203,
                                    Chi4n=4.712021514075524, Chi4v=4.712021514075524, HallKierAlpha=-2.3299999999999996,
                                    Ipc=3746809.9601530447, Kappa1=19.00679023622427, Kappa2=8.356363444273022,
                                    Kappa3=3.925173476821331, LabuteASA=167.00458662052273, PEOE_VSA1=9.473725907600098,
                                    PEOE_VSA10=0.0, PEOE_VSA11=17.28226861293275, PEOE_VSA12=0.0, PEOE_VSA13=0.0,
                                    PEOE_VSA14=0.0, PEOE_VSA2=9.694446914922299, PEOE_VSA3=0.0, PEOE_VSA4=0.0,
                                    PEOE_VSA5=0.0, PEOE_VSA6=30.33183534230805, PEOE_VSA7=67.9503424700078,
                                    PEOE_VSA8=18.026113943770966, PEOE_VSA9=14.219595082555067,
                                    SMR_VSA1=14.268263091671919, SMR_VSA10=5.783244946364939, SMR_VSA2=0.0,
                                    SMR_VSA3=4.899909730850478, SMR_VSA4=11.835812092322787, SMR_VSA5=32.22804289761661,
                                    SMR_VSA6=27.30910789438022, SMR_VSA7=59.15492395432226, SMR_VSA8=0.0,
                                    SMR_VSA9=11.49902366656781, SlogP_VSA1=9.473725907600098, SlogP_VSA10=0.0,
                                    SlogP_VSA11=11.49902366656781, SlogP_VSA12=0.0, SlogP_VSA2=37.99226257159563,
                                    SlogP_VSA3=12.965578028838586, SlogP_VSA4=11.835812092322787,
                                    SlogP_VSA5=40.74735652794084, SlogP_VSA6=42.46456947923127, SlogP_VSA7=0.0,
                                    SlogP_VSA8=0.0, SlogP_VSA9=0.0, TPSA=38.769999999999996, EState_VSA1=0.0,
                                    EState_VSA10=4.794537184071822, EState_VSA11=0.0, EState_VSA2=11.701150992526333,
                                    EState_VSA3=17.416929712729203, EState_VSA4=43.60281544698373,
                                    EState_VSA5=18.405094737549014, EState_VSA6=14.219595082555067,
                                    EState_VSA7=12.13273413692322, EState_VSA8=35.23174507315853,
                                    EState_VSA9=9.473725907600098, VSA_EState1=10.773646631006095, VSA_EState10=0.0,
                                    VSA_EState2=15.471438518707707, VSA_EState3=0.0, VSA_EState4=3.3088814785703318,
                                    VSA_EState5=2.3820563135483286, VSA_EState6=14.515899250917201,
                                    VSA_EState7=4.189755871867163, VSA_EState8=3.2689293059503055,
                                    VSA_EState9=3.256059296099534, FractionCSP3=0.4583333333333333, HeavyAtomCount=28,
                                    NHOHCount=0, NOCount=4, NumAliphaticCarbocycles=1, NumAliphaticHeterocycles=1,
                                    NumAliphaticRings=2, NumAromaticCarbocycles=2, NumAromaticHeterocycles=0,
                                    NumAromaticRings=2, NumHAcceptors=4, NumHDonors=0, NumHeteroatoms=4,
                                    NumRotatableBonds=6, NumSaturatedCarbocycles=0, NumSaturatedHeterocycles=1,
                                    NumSaturatedRings=1, RingCount=4, MolLogP=4.361100000000004,
                                    MolMR=110.13050000000004, fr_Al_COO=0, fr_Al_OH=0, fr_Al_OH_noTert=0, fr_ArN=0,
                                    fr_Ar_COO=0, fr_Ar_N=0, fr_Ar_NH=0, fr_Ar_OH=0, fr_COO=0, fr_COO2=0, fr_C_O=1,
                                    fr_C_O_noCOO=1, fr_C_S=0, fr_HOCCN=0, fr_Imine=0, fr_NH0=1, fr_NH1=0, fr_NH2=0,
                                    fr_N_O=0, fr_Ndealkylation1=0, fr_Ndealkylation2=1, fr_Nhpyrrole=0, fr_SH=0,
                                    fr_aldehyde=0, fr_alkyl_carbamate=0, fr_alkyl_halide=0, fr_allylic_oxid=0,
                                    fr_amide=0, fr_amidine=0, fr_aniline=0, fr_aryl_methyl=0, fr_azide=0, fr_azo=0,
                                    fr_barbitur=0, fr_benzene=2, fr_benzodiazepine=0, fr_bicyclic=1, fr_diazo=0,
                                    fr_dihydropyridine=0, fr_epoxide=0, fr_ester=0, fr_ether=2, fr_furan=0,
                                    fr_guanido=0, fr_halogen=0, fr_hdrzine=0, fr_hdrzone=0, fr_imidazole=0, fr_imide=0,
                                    fr_isocyan=0, fr_isothiocyan=0, fr_ketone=1, fr_ketone_Topliss=1, fr_lactam=0,
                                    fr_lactone=0, fr_methoxy=2, fr_morpholine=0, fr_nitrile=0, fr_nitro=0,
                                    fr_nitro_arom=0, fr_nitro_arom_nonortho=0, fr_nitroso=0, fr_oxazole=0, fr_oxime=0,
                                    fr_para_hydroxylation=0, fr_phenol=0, fr_phenol_noOrthoHbond=0, fr_phos_acid=0,
                                    fr_phos_ester=0, fr_piperdine=1, fr_piperzine=0, fr_priamide=0, fr_prisulfonamd=0,
                                    fr_pyridine=0, fr_quatN=0, fr_sulfide=0, fr_sulfonamd=0, fr_sulfone=0,
                                    fr_term_acetylene=0, fr_tetrazole=0, fr_thiazole=0, fr_thiocyan=0, fr_thiophene=0,
                                    fr_unbrch_alkane=0, fr_urea=0)
        mol_descriptors = mol.calculate_descriptors()
        self.assertEqual(mol_descriptors, expected_descriptors)


if __name__ == '__main__':
    unittest.main()
