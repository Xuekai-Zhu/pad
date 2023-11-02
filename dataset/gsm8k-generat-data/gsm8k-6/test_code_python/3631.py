def solution():
    # Calculate how many shoes Codger currently has
    current_shoes = 3  # Codger has 3 feet

    # Calculate how many shoes he needs to buy
    desired_shoes = 5 * 3  # Codger wants 5 complete 3-piece sets of shoes
    needed_shoes = desired_shoes - current_shoes

    # Calculate how many pairs of shoes he needs to buy
    pairs_of_shoes = needed_shoes // 2  # Stores sell shoes in pairs

    result = pairs_of_shoes
    return result

print(solution())