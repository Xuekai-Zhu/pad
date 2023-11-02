def solution():
    """There are six peregrine falcons and 40 pigeons nesting in Malcolm's skyscraper. Each pigeon has 6 chicks. If the peregrines eat 30% of the pigeons, how many pigeons are left?"""
    falcons = 6
    pigeons = 40
    chicks_per_pigeon = 6
    chicks_total = pigeons * chicks_per_pigeon
    eaten_pigeons = int(pigeons * 0.3)
    left_pigeons = pigeons - eaten_pigeons
    result = left_pigeons
    return result

print(solution())