include .env

create-venv:
	( \
		python3 -m venv venv; \
	)

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt
	python3 -m pip install --upgrade prodigy -f "https://${PRODIGY_KEY}@download.prodi.gy"

download:
	wget https://zenodo.org/record/3251557/files/corpus-webis-clickbait-16.zip
	mkdir data
	unzip corpus-webis-clickbait-16.zip
	cp -a webis-clickbait-16/* data
	rm -rf corpus-webis-clickbait-16.zip
	rm -r webis-clickbait-16

clean-cache:
	rm -rf */__pycache__/*
	rm -rf .ipynb_checkpoints

clean-files:
	rm -vr data
	rm -vr assets
	rm -vr corpus
	rm -vr training
	rm -vr packages

clean-venv:
	rm -r venv

mark:
	python -m prodigy mark clickbait-mark data/tweets-textcat.jsonl --view-id image_manual

image.manual:
	python -m prodigy image.manual clickbait-images data/tweets-textcat.jsonl --label CLICKBAIT --remove-base64

html:
	python -m prodigy html clickbait-html data/tweets-textcat.jsonl --view-id classification	