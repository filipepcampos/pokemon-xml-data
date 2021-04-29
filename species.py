import requests
from dict2xml import dict2xml
from config import *

def parseStats(data):
    statsDict = {}
    for stat in data:
        name = stat["stat"]["name"]
        statsDict[name] = stat["base_stat"]
    return statsDict

def parseMoves(data):
    dataDict = {}
    for moveData in data:
        correctVersion = [i for i in moveData["version_group_details"] if i["version_group"]["name"] == VERSION]
        if(len(correctVersion) == 0):
            continue
        versionGroup = correctVersion[0]

        if(versionGroup["move_learn_method"]["name"] == "level-up"):
            levelLearnt = versionGroup["level_learned_at"]
            moveId = moveData["move"]["url"].split("/")[-2]
            dataDict[levelLearnt] = moveId
    return dataDict

def parseSingleSpecies(data):
    url = data['url'].replace("pokemon-species", "pokemon")
    r = requests.get(url)
    data = r.json()
    
    pokeId = data["id"]

    dataDict = {}    
    dataDict["name"] = data["name"]
    dataDict["base_exp"] = data["base_experience"]
    dataDict["stats"] = parseStats(data["stats"])
    dataDict["moves"] = parseMoves(data["moves"])
    return pokeId, dataDict


def parseSpecies(data):
    totalN = len(data)
    print(f"Reading Species ({totalN} species in total)")
    N = 0

    dataDict = {}
    for speciesData in data:
        i, j = parseSingleSpecies(speciesData)
        dataDict[i] = j
        if(N % 10 == 0):
            print(f"  {N}/{totalN}")
        N += 1
        
    print("Writing species to XML")
    xml = dict2xml(dataDict)
    with open("species.xml", "w+") as file:
        file.write(xml)
