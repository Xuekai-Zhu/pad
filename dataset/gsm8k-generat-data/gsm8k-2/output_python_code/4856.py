def solution():
    """There are six peregrine falcons and 40 pigeons nesting in Malcolm's skyscraper. Each pigeon has 6 chicks. If the peregrines eat 30% of the pigeons, how many pigeons are left?"""
    peregrine_falcons = 6
    pigeons = 40
    chicks_per_pigeon = 6
    total_chicks = pigeons * chicks_per_pigeon
    eaten_pigeons = int(0.3 * pigeons)
    remaining_pigeons = pigeons - eaten_pigeons
    total_remaining_birds = remaining_pigeons + total_chicks + peregrine_falcons
    result = remaining_pigeons
    return result

print(solution())