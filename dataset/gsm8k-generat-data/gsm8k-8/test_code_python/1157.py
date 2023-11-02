def solution():
    # Calculate the total weight of Tony's current load
    total_weight = 10 + 2 * 5 + 8 + 3 * 2
    remaining_weight = 50 - total_weight

    # Determine the weight of one pair of underwear
    underwear_weight = 4
    pair_weight = 2 * underwear_weight

    # Calculate the maximum number of pairs of underwear Tony can add
    max_pairs = remaining_weight // pair_weight
    result = max_pairs
    return result

print(solution())