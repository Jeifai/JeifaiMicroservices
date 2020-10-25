import sys
import json
import nltk
import geograpy
from geograpy.extraction import Extractor

sys.path.append('lib/')
nltk.data.path.append('lib/nltk_data/')


def extract_country_and_city(request):
    input = str(request.args.get('input'))
    e=Extractor(text=input)
    places = e.find_entities()
    return json.dumps({"status": "success","countries": places})
    '''
    countries = []
    for place in places:
        city=geograpy.locateCity(place)
        country=city.country.iso
        countries.append(country)
    s_countries = ','.join(list(set(countries)))
    return json.dumps({"status": "success","countries": s_countries})
    '''

if __name__ == "__main__":
	print(extract_country_and_city("Welcome in Milan"))