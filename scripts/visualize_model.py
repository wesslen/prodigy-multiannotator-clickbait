import spacy_streamlit
import streamlit as st
from clumper import Clumper
import pandas as pd

def main(models: str, default_text: str):
    #models = [name.strip() for name in models.split(",")]
    clump = Clumper.read_jsonl("assets/multilabel_dev.jsonl")
    row = st.slider("Dev record", min_value=0, max_value=len(clump), value=0, step=1)
    #models = ["en_core_web_sm"]
    text = clump.collect()[row]["text"]
    cats = clump.collect()[row]["cats"]
    st.write(cats)
    #default_text = "Sundar Pichai is the CEO of Google."
    spacy_streamlit.visualize(models, text, visualizers=["textcat"])
    #spacy_streamlit.visualize(models, default_text, visualizers=["textcat"])


if __name__ == "__main__":
    try:
        models = ["training/multilabel/model-best/","training/multilabel/model-last/","training/textcat/model-best/","training/textcat/model-last/"]
        default_text = "23 Mexican breakfast that'll make every morning a freakin' fiesta!"
        main(models, default_text)
    except SystemExit:
        pass