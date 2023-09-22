import numpy
import PIL
import pandas

pl_clubs_players = {
    "Chelsea":["Jackson", "Enzo", "Colwil"],
    "Liverpool":["Salah", "Nunez", "Trent"],
    "Arsenal":["Jesus", "Saka", "Rice"],
    "City": ["Haaland", "Alvarez", "Foden"],
    "Brighton": ["Mitoma", "Estupinian", "March"],
}

p = pandas.DataFrame(pl_clubs_players)

with open("Premier_league_data.json", "w") as F:
    F.write(p.to_json(orient="split", indent=True))

F.close()
print(p)
