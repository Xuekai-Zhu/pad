def solution():
    
    total_beakers = 22
    copper_beakers = 8
    drops_per_copper_beaker = 3
    total_copper_drops = copper_beakers * drops_per_copper_beaker
    total_non_copper_beakers_tested = (45 - total_copper_drops) / 3
    non_copper_beakers_tested = total_beakers - copper_beakers
    result = non_copper_beakers_tested - total_non_copper_beakers_tested
    return result

print(solution())