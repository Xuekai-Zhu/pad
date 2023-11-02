def solution():
    # Calculate the number of packs needed for each theme
    vampire_packs = 11 // 5  # round down to whole packs
    pumpkin_packs = 14 // 5  # round down to whole packs

    # Calculate the number of individual bags needed for each theme
    vampire_individuals = 11 % 5  # remaining number of bags needed after purchasing packs
    pumpkin_individuals = 14 % 5  # remaining number of bags needed after purchasing packs

    # Calculate the total cost of buying packs of each theme
    pack_cost = (vampire_packs + pumpkin_packs) * 3

    # Calculate the total cost of buying individual bags of each theme
    individual_cost = vampire_individuals + pumpkin_individuals

    # Calculate the least amount of money the teacher can spend
    total_cost = pack_cost + individual_cost

    result = total_cost
    return result

print(solution())