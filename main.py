import requests
from moves import parseMoves
from species import parseSpecies
from config import *

url = f"https://pokeapi.co/api/v2/generation/{GENERATION}"

def main():
    r = requests.get(url)
    data = r.json()

    parseMoves(data["moves"])
    parseSpecies(data["pokemon_species"])

if __name__ == "__main__":
    main()