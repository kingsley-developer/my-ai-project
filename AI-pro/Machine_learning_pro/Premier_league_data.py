import pandas

def load_data(out_json_file_dir: str = ""):
    pl_clubs_players = {
        "Chelsea": ["Jackson", "Enzo", "Colwil"],
        "Liverpool": ["Salah", "Nunez", "Trent"],
        "Arsenal": ["Jesus", "Saka", "Rice"],
        "City": ["Haaland", "Alvarez", "Foden"],
        "Brighton": ["Mitoma", "Estupinian", "March"],
    }
    p = pandas.DataFrame(pl_clubs_players)
    try:
        if out_json_file_dir == "":
            return

        with open(out_json_file_dir, "w") as F:
            F.write(p.to_json(orient="split", indent=True))
        F.close()
        print(p)
    except Exception as error:
        print(error)
