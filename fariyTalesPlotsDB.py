
import requests
import json
import wikipedia

import re

def openJsonFile(name):
    with open(name) as json_file:
        return json.load(json_file)

def getFiles():
    fairys = []
    for arr in openJsonFile("./fairyTalesNames.json"):
        fairys.append(arr['name'])
    return fairys

def getPlots(raw_content):
    section_title_re = re.compile("^=+\s+.*\s+=+$")
    content = []
    take = False
    for l in raw_content.splitlines():
        line = l.strip()
        if "== Synopsis ==".lower() in line.lower():
            take = True
            continue
        if "== Plot ==".lower() in line.lower():
            print("in plot")
            take = True
            continue
        if "== Story ==".lower() in line.lower():
            take = True
            continue
        if section_title_re.match(line):
            take = False
        if take:
            content.append(line)
    content = '\n'.join(content) + '\n'
    
    return content

fairys = getFiles()

miss_count = 0
fairys_plots = []
for fairy in fairys:
    try:
        fariy_plot = getPlots(wikipedia.page(fairy).content)
        fairys_plots.append(fariy_plot)
    except:
        miss_count+=1
    
open("./" + "fariyTalesPlots.json", "w").write(json.dumps(fairys_plots, indent=4))
print("there are " +str(miss_count)+ " fairy tales without plot in Wiki")