import json
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
    dataDict["priority"] = data["priority"]
    dataDict["description"] = data["flavor_text_entries"][0]["flavor_text"]
    dataDict["name"] = [i["name"] for i in data["names"] if i["language"]["name"] == 'en'][0]
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
    xml = dict2xml(dataDict)
    with open("moves.xml", "w+") as file:
        file.write(xml)