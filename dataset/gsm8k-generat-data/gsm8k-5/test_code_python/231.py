def solution():
    total_beakers = 22  # There are 22 beakers in the fume hood
    copper_beakers = 8  # 8 of the beakers have copper ions in them
    drops_per_copper_beaker = 3  # 3 drops are needed to turn the liquid blue in a beaker with copper ions
    total_drops = 45  # 45 drops were used before all 8 copper beakers were found

    # Calculate the total drops used on copper beakers
    drops_on_copper_beakers = copper_beakers * drops_per_copper_beaker

    # Calculate the drops used on non-copper beakers
    drops_on_non_copper_beakers = total_drops - drops_on_copper_beakers

    # Calculate the number of non-copper beakers tested
    non_copper_beakers_tested = drops_on_non_copper_beakers / 3

    # Calculate the number of copper beakers tested
    copper_beakers_tested = copper_beakers - (total_beakers - non_copper_beakers_tested)

    result = non_copper_beakers_tested
    return result

print(solution())