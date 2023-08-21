from transformers import pipeline
import urllib.request
### Disable Certificate Verification
from urllib.request import urlopen
import ssl

from bs4 import BeautifulSoup

from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

class SummarizeRequest(BaseModel): 
    url: str
    
# mute tensorflow complaints (Disable Tensorflow debugging information)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# q: what is the meaning of 'TF_CPP_MIN_LOG_LEVEL'?
# a: https://stackoverflow.com/questions/35911252/disable-tensorflow-debugging-information

def extract_from_url(url):
    text = ""
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' + \
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        } 
    )
    ### Disable Certificate Verification
    # html = urllib.request.urlopen(req)
    context = ssl._create_unverified_context()
    html = urllib.request.urlopen(req, context=context)

    parser = BeautifulSoup(html, 'html.parser')
    for paragraph in parser.find_all('p'):
        text += paragraph.text
    return text

def process(text):
<<<<<<< HEAD
    summarizer = pipeline("summarization", model='t5-base', tokenizer='t5-base', truncation=True, framework="tf")
=======
    summarizer = pipeline("summarization", model='t5-small', tokenizer='t5-base', truncation=True, framework="tf")
>>>>>>> d9526b166f0c810092079359184fd24ea754d6d8
    result = summarizer(text, min_length=180, truncation=True)
    return result[0]['summary_text']

@app.post("/summarize")
def summarize(request: SummarizeRequest):
    url = request.url
    text = extract_from_url(url)
<<<<<<< HEAD
    return Response(text) 
=======
    # if url:
    #     text = extract_from_url(url)
    # elif file:
    #     with open(file, 'r') as f: 
    #         text = f.read()
    # else:
    #     raise Exception('No input provided')
    return process(text)
>>>>>>> d9526b166f0c810092079359184fd24ea754d6d8


@app.get("/")
def root():
    return Response("<H1>Summarizer API</H1>", media_type="text/html")


