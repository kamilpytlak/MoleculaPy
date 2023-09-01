<h1 align="center">
  🧪 MoleculaPy 🧪 
  <br>
</h1>

<h4 align="center">A command-line application that utilizes the RDKit library to compute molecular descriptors and fingerprints, aiding in the analysis and characterization of chemical structures.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#contact">Contact</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<p align="center">MoleculaPy is a powerful command-line interface (CLI) application developed in Python, designed for chemoinformatics enthusiasts and researchers. Leveraging the renowned RDKit library, MoleculaPy empowers users to effortlessly compute a diverse set of molecular descriptors and fingerprints for compounds specified in the SMILES (Simplified Molecular Input Line Entry System) format, all within the convenience of their terminal.</p>

## Key Features
*  📝 **SMILES Compatibility**: MoleculaPy seamlessly processes chemical data in the SMILES format, the industry-standard notation for representing molecular structures.


*  🧬 **Comprehensive Descriptors**: The application provides an extensive set of molecular descriptors, in a total number of 209. This breadth empowers users to gain deep insights into the properties and characteristics of chemical compounds.


*  🔍 **Fingerprint Generation**: MoleculaPy offers robust functionality for generating molecular fingerprints, a critical component for tasks such as similarity analysis and virtual screening: n-dimensional Atom, Morgan, RDKit, Topological and 166-dimensional MACCS.


*  📁 **CSV File Support**: Import and process large datasets of compounds effortlessly with MoleculaPy's CSV file support, streamlining high-throughput data analysis.


*  🧪 **Scientific Accuracy**: MoleculaPy relies on the RDKit library, known for its scientific rigor and reliability in chemoinformatics, ensuring trustworthy results for research and analysis.


*  🖥️ **User-Friendly Command Line**: The CLI interface is designed to be user-friendly and intuitive, catering to both seasoned researchers and newcomers in the field.


*  🧂 **Salt Removal Option**: MoleculaPy offers users the flexibility to choose whether they want to remove salts from molecules during processing. This feature is particularly valuable when working with complex chemical datasets, allowing for cleaner and more accurate analyses.


*  📄 **Logging for Transparency**: MoleculaPy integrates a robust logging system that maintains detailed records of application activities. This ensures transparency and facilitates tasks such as debugging, progress tracking, auditing, and reproducibility.

## Installation
To install this app, just type in your CLI the following command:
```commandline
pip install moleculapy
```

Then make sure that the installation process went correctly by typing `moleculepy -h` in the CLI.
```commandline
>>> moleculepy -h

usage: MoleculaPy [-h] [--method {descriptors,fingerprints}] [--fp_type {Atom,MACCS,Morgan,Topological,RDKit}]
                  [--remove_salt | --no-remove_salt] [--n_bits N_BITS]
                  input_file output_file

Calculate molecular descriptors and fingerprints for molecules provided in a CSV file.

positional arguments:
  input_file            Path to the input file
  output_file           Path to the output file

options:
  -h, --help            show this help message and exit
  --method {descriptors,fingerprints}
                        (Optional) Calculation method: descriptors or fingeprints (default: descriptors)
  --fp_type {Atom,MACCS,Morgan,Topological,RDKit}
                        (Optional) Fingerprint type (default: Morgan)
  --remove_salt, --no-remove_salt
                        (Optional) Remove salts from SMILE. (default: --remove_salt)
  --n_bits N_BITS       (Optional) Number of bits of a given fingerprints type (default: 2048)
```

## How To Use
The application is fully compatible with Python 3.9+.

### Setting Up

By default, the program requires two arguments: `input_file` and `output_file`. Both are paths - the CSV file containing SMILES molecules and the output file, respectively.

Suppose we have a file `smiles_samples.csv`, which contains SMILES molecules (and other information, in this case it is not important). The column containing SMILES must be named "SMILES" (case-insensitive).

### Calculate molecular descriptors
To calculate molecular descriptors, we do not need to specify optional parameters. Thus, it is sufficient that we call:

```commandline
moleculapy --input_file .\smiles_sample.csv --output_file .\smiles_desc_output.csv
```

By default, MoleculaPy removes salts from chemical compounds, To oppose this, you must use the `--no-remove_salt parameter`:

```commandline
moleculapy --input_file .\smiles_sample.csv --output_file .\smiles_desc_output.csv --no-remove-salt
```

### Calculate fingerprints
With MoleculaPy, you can calculate various n-dimensional vectors of molecules, known as fingerprints: n-dimensional Atom, Morgan, RDKit, Topological and 166-dimensional MACCS.

To do this, you need to take care of two optional arguments: `--method` and `--fp_type`. The first argument specifies the calculation method (molecular descriptors or fingerprints), and the second one -- the fingerprint type.

For example, if you want to calculate 2048-dimensional Morgan fingerprints:

```commandline
moleculapy --input_file .\smiles_sample.csv --output_file .\smiles_morgan_output.csv --method fingerprints --fp_type Morgan
```

Atom, Morgan, RDKit and Topological compute as 2048-dimensional vectors by default, and MACCS computes as 166-dimensional vectors. If you want to change it, you can specify the another optional parameter `--n_bits`.

For example, if you want to calculate 512-dimensional fingerprints vectors of Atom type:
```commandline
moleculapy --input_file .\smiles_sample.csv --output_file .\smiles_atom_output.csv --method fingerprints --fp_type Atom --n_bits 512
```

### Logging
All calculations performed by the application are logged. The logs are stored in the `logs` folder in the path where the application was installed. The path to the logs will be displayed in the CLI after the calculation session is completed.

## Contact
If you have any problems, ideas or general feedback, please don't hesitate to contact me at [kam.pytlak@gmail.com](mailto:kam.pytlak@gmail.com). I'd really appreciate it!

## Credits

This software uses the following open source packages:

- [pandas](https://pandas.pydata.org/)
- [RDKit](https://www.rdkit.org/docs/index.html#)
- [tqdm](https://github.com/tqdm/tqdm)

## License
MIT

---

> GitHub [@kamilpytlak](https://github.com/kamilpytlak) &nbsp;&middot;&nbsp;
> LinkedIn [kamil-pytlak](https://www.linkedin.com/in/kamil-pytlak/)
