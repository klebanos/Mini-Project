import json

from SPARQLWrapper import SPARQLWrapper, JSON

def get_results(endpoint_url, query):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def create_fairy_tale_json(fairy_tales):
    query = """SELECT ?fairy_tale ?fairy_taleLabel WHERE {
    ?fairy_tale wdt:P31 wd:Q699.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }  """
    endpoint_url = "https://query.wikidata.org/sparql"
    results = get_results(endpoint_url, query)
    print("--------------start query for fairy tales:")
    for result in results["results"]["bindings"]:
      if(not result['fairy_taleLabel']['value'].startswith("Q")):
        fairy_tale = {}
        name = result['fairy_taleLabel']['value']
        fairy_tale["name"] = name
        fairy_tales.append(fairy_tale)

    print("--------------creating json file: fairyTales.json")
    print("there are " + str(len(fairy_tales)) + " items")
    open("./" + "fairyTalesNames.json", "w").write(json.dumps(fairy_tales, indent=4))


def open_json_file(name):
    with open(name) as json_file:
        return json.load(json_file)


def get_fairy_tales_new():
    fairy_tales = []
    create_fairy_tale_json(fairy_tales)
  
get_fairy_tales_new()