# Prodigy project for multi-label/task of multiannotators for Webis-16 Clickbait

This project contains code for running experiments on reframing Webis-16 Clickbait dataset [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.3251557.svg)](http://dx.doi.org/10.5281/zenodo.3251557) as a multi-label/task problem by annotators consistent with [Davani et al., 2022](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00449/109286/Dealing-with-Disagreements-Looking-Beyond-the).

## Installation

The installation process is automated via `make`.

```bash
# Create virtual environment (optional, recommended)
make create-venv
# Install all dependencies
make install
# Download the zenodo dataset
make download
```

In order for the install to work, you'll need to
add a `.env` file to the root of the project that
contains your Prodigy license key. It should look
something like:

```
PRODIGY_KEY="1234-ABCD-5678-EFGH"
```

## Contents 

The project has a few notable files/folders: 

- The `data/problems` folder contains `.json`, `.html`, and `.jpg` files. This is empty by default but users can run the `make download` to download the files.

- Annotation ground truth are provided as `.csv` files in the `data/truth` folder.