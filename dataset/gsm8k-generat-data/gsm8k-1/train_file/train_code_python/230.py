def solution():
    """A laboratory has 22 beakers of liquid in a fume hood, and 8 of the beakers have copper ions in them. Adding three drops of a solution will turn the liquid in a beaker blue if there are copper ions present. If the beakers are tested one by one for copper ions and 45 drops are used before all 8 beakers with copper ions are found, how many beakers without copper ions were tested?"""
    total_beakers = 22
    beakers_with_copper = 8
    drops_per_beaker = 3
    drops_to_find_all_copper_beakers = beakers_with_copper * drops_per_beaker
    drops_for_other_beakers = 45 - drops_to_find_all_copper_beakers
    beakers_without_copper = drops_for_other_beakers / drops_per_beaker
    result = beakers_without_copper
    return result

print(solution())