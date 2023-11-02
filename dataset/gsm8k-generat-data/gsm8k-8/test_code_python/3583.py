def solution():
    # Define the ratio of seed to fertilizer
    seed_to_fertilizer_ratio = 3

    # Calculate the total amount of seed and fertilizer used
    total_seed_and_fertilizer = 60

    # Calculate the total amount of seed used by dividing the total by the sum of the ratio
    total_seed = total_seed_and_fertilizer / (1 + seed_to_fertilizer_ratio)

    result = total_seed
    return result

print(solution())