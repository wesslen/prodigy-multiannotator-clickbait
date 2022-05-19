# Prodigy project for multi-label/task of multiannotators for Webis-16 Clickbait

This project contains code for running experiments on reframing Webis-16 Clickbait dataset [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.3251557.svg)](http://dx.doi.org/10.5281/zenodo.3251557) as a multi-label/task problem by annotators consistent with [Davani et al., 2022](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00449/109286/Dealing-with-Disagreements-Looking-Beyond-the).

![](img/davani.png)

Figure from Davani et al., 2022 TACL

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

## Preprocess

The data comes in a distributed folder structure where each subfolder is 2,992 tweets. Each subfolder includes the original `.json` file and (optionally) `.html` and `.jpg` file from a link of the tweet.

After running `make download`, you can preprocess the data by running:

```bash
make preprocess
```

This step will create two new files: `data/tweets-textcat.jsonl` (majority label) and `data/tweets-multilabel.jsonl` (preserve each three annotator's labels).

## Examples

Here are examples of each file:

```bash
#data/tweets-textcat.jsonl
{"text": "RT @BBCNewsMagazine: This 57-storey tower took just 19 days to build http://t.co/J73scxPwEL http://t.co/ITZuJlcRY6", "label": "CLICKBAIT", "answer": "accept", "meta": {"id": 608908946863222785, "created_at": "Thu Jun 11 08:09:40 +0000 2015"}}
```

```bash
#data/tweets-multilabel.jsonl
{"text": "RT @BBCNewsMagazine: This 57-storey tower took just 19 days to build http://t.co/J73scxPwEL http://t.co/ITZuJlcRY6", "cats": {"ANN1": 1.0, "ANN2": 1.0, "ANN3": 0.0}, "meta": {"id": 608908946863222785, "created_at": "Thu Jun 11 08:09:40 +0000 2015"}}
```

Notice this record is an example of a "majority" rule as two annotators selected this as clickbait. 