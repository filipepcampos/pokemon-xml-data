from config import *
from dict2xml import dict2xml
import requests

def parseSingleMove(data):
    url = data['url']
    r = requests.get(url)
    data = r.json()
    
    moveId = int(data["id"])

    dataDict = {}
    dataDict["accuracy"] = data["accuracy"]
    dataDict["power"] = data["power"]
    dataDict["pp"] = data["pp"]

    # TODO: This is stupid, there's no text for versions below gold-silver
    ver = VERSION if VERSION not in ['red-blue', 'yellow'] else 'gold-silver'
    dataDict["description"] = [i for i in data["flavor_text_entries"] if i["language"]["name"] == LANGUAGE and i["version_group"]["name"] == ver][0]["flavor_text"]
    dataDict["name"] = [i["name"] for i in data["names"] if i["language"]["name"] == LANGUAGE][0]
    return moveId, dataDict

    

def parseMoves(data):
    totalN = len(data)
    print(f"Reading Moves ({totalN} moves in total)")
    N = 0

    dataDict = {}
    for moveData in data:
        i, j = parseSingleMove(moveData)
        dataDict[i] = j
        if(N % 10 == 0):
            print(f"  {N}/{totalN}")
        N += 1

    print("Writing Moves to XML")
    outDict = {}
    outDict["moves"] = dataDict
    xml = dict2xml(outDict)
    with open("moves.xml", "w+") as file:
        file.write(xml)