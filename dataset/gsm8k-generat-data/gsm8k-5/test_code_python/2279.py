def solution():
    pairs_of_shoes = 10  # Austin has 10 pairs of dress shoes
    individual_shoes = pairs_of_shoes * 2  # Each pair of dress shoes has 2 individual shoes
    polished_shoes = int(individual_shoes * 0.45)  # Austin has polished 45% of individual shoes

    # Calculate the number of shoes still needing polish
    shoes_remaining = individual_shoes - polished_shoes
    result = shoes_remaining
    return result

print(solution())