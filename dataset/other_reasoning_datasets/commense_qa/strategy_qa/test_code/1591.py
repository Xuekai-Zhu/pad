def solution():
    louvre_material = "limestone"
    nitric_acid_dissolves = "limestone"
    if nitric_acid_dissolves in louvre_material:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())