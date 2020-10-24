import sys
import json
import nltk
import geograpy
from geograpy.extraction import Extractor

sys.path.append('lib/')
nltk.data.path.append('lib/nltk_data/')
nltk.download('punkt')
nltk.download('words')
nltk.download('treebank')
nltk.download('maxent_ne_chunker')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_treebank_pos_tagger')

def extract_country_and_city(request):
    input = request.args.get('input')
    countries = []
    e=Extractor(text=input)
    places=e.find_entities()
    for place in places:
        city=geograpy.locateCity(place)
        country=city.country.iso
        countries.append(country)
    s_countries = ','.join(list(set(countries)))
    return json.dumps({"status": "success","countries": s_countries})

if __name__ == "__main__":
	print(extract_country_and_city("Welcome in Milan"))