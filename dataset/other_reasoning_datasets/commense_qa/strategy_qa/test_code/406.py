def solution():
    yeti_lookalike_animals = ["primates", "bears"]
    prehensile_animals = ["primates"]
    overlap = [animal for animal in yeti_lookalike_animals if animal in prehensile_animals]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())