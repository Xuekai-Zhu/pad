def solution():
    seed_to_fertilizer_ratio = 3  # Each square meter needs three times as much seed as fertilizer
    total_seed_and_fertilizer = 60  # Carson uses 60 gallons of seed and fertilizer combined

    # Calculate the amount of seed and fertilizer used, using the ratio
    total_units = seed_to_fertilizer_ratio + 1  # Ratio of seed to fertilizer is 3:1
    seed_units = seed_to_fertilizer_ratio / total_units
    fertilizer_units = 1 / total_units

    # Calculate the amount of seed used, using the units and total amount
    seed_used = seed_units * total_seed_and_fertilizer
    result = seed_used
    return result

print(solution())