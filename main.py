import json
import requests
from moves import parseMoves
from species import parseSpecies

url = "https://pokeapi.co/api/v2/generation/1"

def main():
    r = requests.get(url)
    data = r.json()

    parseSpecies(data["pokemon_species"])
    parseMoves(data["moves"])

if __name__ == "__main__":
    main()