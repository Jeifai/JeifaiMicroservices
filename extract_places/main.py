import sys
import json
import nltk
import geograpy
from geograpy.extraction import Extractor

sys.path.append('lib/')
nltk.data.path.append('lib/nltk_data/')

def extract_places(request):
    input = str(request.args.get('input'))
    e=Extractor(text=input)
    places = e.find_entities()
    return json.dumps({"status": "success","places": places})

if __name__ == "__main__":
	print(extract_places("Welcome in Milan"))