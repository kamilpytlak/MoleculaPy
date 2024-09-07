# Change Log

---

## 1.1.2
Released on May 5, 2024

### Changed
* Fixed a bug with event capture (logging) preventing the program from running in the console

## 1.1.0
Released on May 5, 2024

### Changed
* Updated dependencies to Python 3.9+ compatible versions

## 1.0.1
Released on September 1, 2023

### Added
* README.md

## 1.0.0
Released on September 1, 2023.

### Added

* The first version of the MoleculaPy CLI application, which provides:
    - calculation of molecular descriptors and fingerprints of molecules written in the SMILES format, provided in a CSV file
    - removing salts from molecules
    - 209 molecular descriptors from the RDKit library
    - four types of fingerprints: n-dimensional Atom, Morgan, Topological, RDKit and 166-dimensional MACCS
    - logging