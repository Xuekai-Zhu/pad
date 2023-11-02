def solution():
    """A laboratory has 22 beakers of liquid in a fume hood, and 8 of the beakers have copper ions in them. Adding three drops of a solution will turn the liquid in a beaker blue if there are copper ions present. If the beakers are tested one by one for copper ions and 45 drops are used before all 8 beakers with copper ions are found, how many beakers without copper ions were tested?"""
    total_beakers = 22
    copper_beakers = 8
    drops_per_copper_beaker = 3
    total_copper_drops = copper_beakers * drops_per_copper_beaker
    total_non_copper_beakers_tested = (45 - total_copper_drops) / 3
    non_copper_beakers_tested = total_beakers - copper_beakers
    result = non_copper_beakers_tested - total_non_copper_beakers_tested
    return result

print(solution())