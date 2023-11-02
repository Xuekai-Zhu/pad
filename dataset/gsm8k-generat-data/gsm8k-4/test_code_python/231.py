def solution():
    """A laboratory has 22 beakers of liquid in a fume hood, and 8 of the beakers have copper ions in them. Adding three drops of a solution will turn the liquid in a beaker blue if there are copper ions present. If the beakers are tested one by one for copper ions and 45 drops are used before all 8 beakers with copper ions are found, how many beakers without copper ions were tested?"""
    # Define the number of beakers and beakers with copper ions
    total_beakers = 22
    copper_beakers = 8

    # Define the number of drops needed to detect copper ions in a beaker
    drops_per_copper_beaker = 3

    # Calculate the total number of drops used to find all 8 copper beakers
    total_copper_drops = copper_beakers * drops_per_copper_beaker

    # Calculate the number of non-copper beakers tested
    non_copper_beakers_tested = total_copper_drops // drops_per_copper_beaker - copper_beakers

    result = non_copper_beakers_tested
    return result

print(solution())