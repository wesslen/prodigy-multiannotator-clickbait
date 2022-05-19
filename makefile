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
	rm -rf data

clean-venv:
	rm -rf venv

preprocess:
	python scripts/preprocess.py