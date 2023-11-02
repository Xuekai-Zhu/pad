def solution():
    # Calculate the total weight of the clothes Tony wants to wash
    total_weight = 10 + 2*5 + 8 + 3*2  # Pair of pants, 2 shirts, pair of shorts, and 3 pairs of socks

    # Calculate the remaining weight Tony can add without breaking the rule
    remaining_weight = 50 - total_weight

    # Calculate how many pairs of underwear Tony can add without breaking the rule
    weight_per_pair = 4  # Underwear weighs 4 ounces
    pairs_of_underwear = remaining_weight // weight_per_pair

    result = pairs_of_underwear
    return result

print(solution())