from pprint import pprint
from glob import glob 
import json
import os

jsonlist = glob("logs/privacy/confaide*.json")
outfile = "results/privacy/confaide.json"

model_id = 'llava-v1.5-7b' #ignore
keyname_mapping = {
    "MatchAndScoreEvaluator:pearson_corr": "pearson_corr",
    "MatchAndScoreEvaluator:failure": "failure",
}

results = {}
results['model_id'] = model_id
results['scores'] = {}
for jsonfile in jsonlist:
    filename = os.path.splitext(os.path.basename(jsonfile))[0]
    with open(jsonfile, 'r') as fp:
        data = json.load(fp)

        results['scores'][filename] = {}
        for keyname in keyname_mapping.keys():
            newkeyname = keyname_mapping[keyname]
            results['scores'][filename][newkeyname] = round(data[keyname], 4)

pprint(results)
os.makedirs(os.path.dirname(outfile), exist_ok=True)

with open(outfile, 'w') as fp:
    json.dump(results, fp)