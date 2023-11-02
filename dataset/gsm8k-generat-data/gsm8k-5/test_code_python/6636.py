def solution():
    # First plant produces 50 seeds in 2 months
    # Half of these seeds land on good soil and grow into new plants
    new_plants = 50 / 2

    # Each of these new plants will also produce 50 seeds in 2 months
    total_new_seeds = new_plants * 50

    # Total number of seeds produced by all plants in 2 months
    total_seeds = 50 + total_new_seeds
    result = total_seeds
    return result

print(solution())