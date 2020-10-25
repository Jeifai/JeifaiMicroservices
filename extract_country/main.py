import os
import sys
import json
import geograpy
from geograpy import Locator

path = os.path.dirname(os.path.realpath(__file__))

def extract_country(request):
    input = str(request.args.get('input'))
    city=geograpy.Locator(db_file=path+'/lib/locs.db').locateCity([input])
    country=city.country.iso
    return json.dumps({"status": "success","country": country})

if __name__ == "__main__":
	print(extract_country("Berlin"))