# pre-install
conda create -n RL101 python=3.10.12
conda update --all
conda update conda
conda install -c conda-forge fastapi
conda list | grep -E "transformers|fastapi"


conda config --append channels conda-forge
conda config --show channels
conda install --file requirements.txt


conda install -c conda-forge stable-baselines3


# huggingface
test for huggingface


# Summarization
Summarization CLI tool using HuggingFace
https://youtu.be/DSHfHT5qnGc

> summarize --url https://onesixx.com/huggingface
