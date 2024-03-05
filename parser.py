##
## EPITECH PROJECT, 2024
## parser.py
## File description:
## Parse params
##

import sys

def parse_param(par:str) -> list:
    (parts := par.split("*")).reverse()
    return [float(i) for i in parts]

def parse() -> dict:
    params = sys.argv[1:]
    data = {
        "nums": [],
        "dems": [],
    }

    for i in range(len(params)):
        param = parse_param(params[i])
        if i % 2 == 0:
            data["nums"].append(param)
        else:
            data["dems"].append(param)
    return (data)
