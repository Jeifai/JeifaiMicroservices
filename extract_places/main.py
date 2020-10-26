import sys
import json
import nltk
import geograpy
from geograpy.extraction import Extractor

sys.path.append('lib/')
nltk.data.path.append('lib/nltk_data/')

def extract_places(request):
    try:
        input = str(request.args.get('input'))
    except:
        input = request["input"]

    try:
        e = Extractor(text=input)
        places = e.find_entities()
        return json.dumps({
            "status": "success",
            "places": places
        }, ensure_ascii=False).encode('utf8').decode()
    except Exception as e:
        return json.dumps({
            "status": "ko",
            "error": str(e)
        })

if __name__ == "__main__":
    print(
        extract_places({
            "input": "Münich is a beautiful city"
        }))