<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Multiannotator Experiments

Experiments on multiple annotators with multi-label/task

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Preprocess raw files to jsonl |
| `partition` | Partition jsonl |
| `convert` | Convert the data to spaCy's binary format |
| `ml-train` | Train the multilabel model |
| `tc-train` | Train the textcat model |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model as a pip package |
| `ml-visualize-model` | Visualize the model's output interactively using Streamlit |
| `tc-visualize-model` | Visualize the model's output interactively using Streamlit |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `preprocess-all` | `preprocess` &rarr; `partition` &rarr; `convert` |
| `train` | `ml-train` &rarr; `tc-train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/multilabel_train.jsonl`](assets/multilabel_train.jsonl) | Local | Clickbait training data for multilabels |
| [`assets/multilabel_dev.jsonl`](assets/multilabel_dev.jsonl) | Local | Clickbait development data for multilabels |
| [`assets/textcat_train.jsonl`](assets/textcat_train.jsonl) | Local | Clickbait training data for textcat (Majority) |
| [`assets/textcat_dev.jsonl`](assets/textcat_dev.jsonl) | Local | Clickbait development data for textcat (Majority) |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->

### Project overview

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

- The `data/problems` folder contains `.json`, `.html`, and `.jpg` files. This is empty by default but users can run the `make download` to download the files. The data comes in a distributed folder structure where each subfolder is 2,992 tweets. Each subfolder includes the original `.json` file and (optionally) `.html` and `.jpg` file from a link of the tweet.

- Annotation ground truth are provided as `.csv` files in the `data/truth` folder.

## Instances

Here are instances of each file:

```bash
#data/tweets-textcat.jsonl
{"text": "4 ways the yuccie can find happiness at work:  ", "cats": {"CLICKBAIT": true, "NOT_CLICKBAIT": false}, "meta": {"id": 608955092159590400, "created_at": "Thu Jun 11 11:13:02 +0000 2015"}}
{"text": "\"People are flying blind when it comes to collecting Social Security.\" ", "cats": {"CLICKBAIT": true, "NOT_CLICKBAIT": false}, "meta": {"id": 608302785361256448, "created_at": "Tue Jun 09 16:01:00 +0000 2015"}}
{"text": "Police seize 45k euros from Cristiano Ronaldo's mother in Spain  ", "cats": {"CLICKBAIT": false, "NOT_CLICKBAIT": true}, "meta": {"id": 607984957181575169, "created_at": "Mon Jun 08 18:58:04 +0000 2015"}}
{"text": "Bernie Sanders on the attack ahead of Clinton rally  ", "cats": {"CLICKBAIT": false, "NOT_CLICKBAIT": true}, "meta": {"id": 609440238654619648, "created_at": "Fri Jun 12 19:20:50 +0000 2015"}}
```

```bash
#data/tweets-multilabel.jsonl
{"text": "4 ways the yuccie can find happiness at work:  ", "cats": {"ANN1": 1.0, "ANN2": 1.0, "ANN3": 1.0}, "meta": {"id": 608955092159590400, "created_at": "Thu Jun 11 11:13:02 +0000 2015"}}
{"text": "\"People are flying blind when it comes to collecting Social Security.\" ", "cats": {"ANN1": 1.0, "ANN2": 1.0, "ANN3": 0.0}, "meta": {"id": 608302785361256448, "created_at": "Tue Jun 09 16:01:00 +0000 2015"}}
{"text": "Police seize 45k euros from Cristiano Ronaldo's mother in Spain  ", "cats": {"ANN1": 0.0, "ANN2": 0.0, "ANN3": 1.0}, "meta": {"id": 607984957181575169, "created_at": "Mon Jun 08 18:58:04 +0000 2015"}}
{"text": "Bernie Sanders on the attack ahead of Clinton rally  ", "cats": {"ANN1": 0.0, "ANN2": 0.0, "ANN3": 0.0}, "meta": {"id": 609440238654619648, "created_at": "Fri Jun 12 19:20:50 +0000 2015"}}
```

Four examples with a range of annotator agreement out of three annotators from top (100% agree clickbait) to bottom (0% agree clickbait).