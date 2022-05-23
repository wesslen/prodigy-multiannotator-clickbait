"""Convert raw text files to JSONL format."""

import typer
import json
from pathlib import Path
import glob
import srsly
import random
from clumper import Clumper
import re

def export_jsonl(output_path: Path, data):
    json_lines = [json.dumps(l) for l in data]
    # this will shuffle the sentences
    #random.shuffle(json_lines)
    #json_dev_data = '\n'.join(json_lines[0:1000])
    #json_train_data = '\n'.join(json_lines[1001:])
    json_data = '\n'.join(json_lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json_data)


def read_labels():

    annA = Clumper.read_csv("data/truth/annotatorA.csv", fieldnames=["id","labelA"])
    annB = Clumper.read_csv("data/truth/annotatorB.csv", fieldnames=["id","labelB"])
    annC = Clumper.read_csv("data/truth/annotatorC.csv", fieldnames=["id","labelC"])
    majority = Clumper.read_csv("data/truth/majority.csv", fieldnames=["id","labelMajority"])

    result = annA.inner_join(annB, mapping={"id": "id"})
    result = result.inner_join(annC, mapping={"id": "id"})
    result = result.inner_join(majority, mapping={"id": "id"})

    return result

def process_raw(input_path: Path):

    folders = glob.glob(input_path)
    labels = read_labels()
    textcat_data = []
    multilabel_data = []

    for i in folders:
        files = glob.glob(i + "*/*")
        json_file = [f for f in files if ".json" in f]
        #html_file = [f for f in files if ".html" in f]
        #image_file = [f for f in files if ".png" in f]
        j = srsly.read_json(json_file[0])
        l = (Clumper(labels)
            .keep(lambda d: d['id'] == str(j["id"]))
            .collect())
        
        if json_file:
            textcat_data.append({"text": re.sub(r'http\S+', '', j["text"]),  
                               #"image": image_file[0], 
                               #"html": html_file[0], 
                               #"label": "CLICKBAIT",
                               #"answer": "accept" if l[0]['labelMajority']=='clickbait' else "reject",
                               "cats": {"CLICKBAIT": True if l[0]['labelMajority']=='clickbait' else False, "NOT_CLICKBAIT": False if l[0]['labelMajority']=='clickbait' else True},
                               "meta": {"id": j["id"], "created_at": j["created_at"]}})
            multilabel_data.append({"text": re.sub(r'http\S+', '', j["text"]), 
                                #"image": image_file[0], 
                                #"html": html_file[0], 
                                "cats": {"ANN1": 1.0 if l[0]['labelA'] in ['strong','medium'] else 0.0, "ANN2": 1.0 if l[0]['labelB'] in ['strong','medium'] else 0.0, "ANN3": 1.0 if l[0]['labelC'] in ['strong','medium'] else 0.0},
                                "meta": {"id": j["id"], "created_at": j["created_at"]}})    

    return textcat_data, multilabel_data
    
def preprocess():
    textcat_data, multilabel_data = process_raw("data/problems/*")

    export_jsonl("assets/tweets-textcat.jsonl", textcat_data)
    export_jsonl("assets/tweets-multilabel.jsonl", multilabel_data)

if __name__ == "__main__":
    typer.run(preprocess)