def solution():
    jesus_walked_on_water = True
    jesus_virgin_birth = True
    jesus_killed_beside_thieves = True
    horus_walked_on_water = True
    horus_virgin_birth = True
    horus_executed_beside_thieves = True
    if jesus_walked_on_water == horus_walked_on_water and jesus_virgin_birth == horus_virgin_birth and jesus_killed_beside_thieves == horus_executed_beside_thieves:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())