def solution():
    total_beakers = 22
    num_copper_beakers = 8
    drops_per_copper_beaker = 3
    total_drops = 45

    # Calculate the total drops used in copper beakers
    total_copper_drops = num_copper_beakers * drops_per_copper_beaker

    # Calculate the drops used in non-copper beakers
    non_copper_drops = total_drops - total_copper_drops

    # Calculate the number of non-copper beakers tested
    num_non_copper_beakers = non_copper_drops // drops_per_copper_beaker

    result = num_non_copper_beakers
    return result

print(solution())