def solution():
    seed_to_fertilizer_ratio = 3
    total_gallons = 60

    # Calculate the total amount of seed and fertilizer combined
    total_seed_and_fertilizer = total_gallons / (seed_to_fertilizer_ratio + 1)

    # Calculate the amount of seed used
    seed_used = total_seed_and_fertilizer * seed_to_fertilizer_ratio
    result = seed_used
    return result

print(solution())