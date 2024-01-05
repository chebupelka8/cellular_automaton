from Engine import *
import json


WINDOW_SIZE = Vec2(1000, 1000)
B, S = [3, 5, 6, 7, 8], [5, 6, 7, 8] # born, still live,

def set_rules(__b: list, __s: list) -> None:
    global B, S

    B = __b
    S = __s

def get_rules() -> list[list]:
    return [B, S]

# def get_rules() -> list[list]:
#     with open("source/config/data.json", "r", encoding="utf-8") as file:
#         data = json.load(file)

#     return list(data["--rules"].values())

# def set_rules(__b: list, __s: list) -> None:
#     with open("source/config/data.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
    
#     data["--rules"] = {
#         "B": __b,
#         "S": __s
#     }

#     with open("source/config/data.json", "w", encoding="utf-8") as file:
#         json.dump(data, file, indent=4)