def solution():
    """Carson is covering the high school football field with grass seed. Each square meter needs three times as much seed as fertilizer. If Carson uses 60 gallons of seed and fertilizer combined, how many gallons of seed does he use?"""
    # Define the seed to fertilizer ratio
    seed_to_fertilizer_ratio = 3

    # Calculate the total amount of seed and fertilizer used
    total_seed_and_fertilizer = 60

    # Define the amount of seed used per square meter
    seed_per_square_meter = seed_to_fertilizer_ratio + 1

    # Calculate the amount of seed used to cover the entire football field
    square_meters = total_seed_and_fertilizer / seed_per_square_meter
    seed_used = square_meters * seed_to_fertilizer_ratio

    # return the answer
    result = seed_used
    return result

print(solution())