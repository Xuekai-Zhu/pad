def solution():
    
    total_beakers = 22
    beakers_with_copper = 8
    drops_per_beaker = 3
    drops_to_find_all_copper_beakers = beakers_with_copper * drops_per_beaker
    drops_for_other_beakers = 45 - drops_to_find_all_copper_beakers
    beakers_without_copper = drops_for_other_beakers / drops_per_beaker
    result = beakers_without_copper
    return result

print(solution())