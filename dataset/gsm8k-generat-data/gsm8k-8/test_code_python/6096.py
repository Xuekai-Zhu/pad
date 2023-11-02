def solution():
    # Define the original weight of the steak
    original_weight = 30

    # Calculate the weight of the burned portion
    burned_weight = original_weight / 2

    # Calculate the weight of the remaining portion
    remaining_weight = original_weight - burned_weight

    # Calculate the weight of the portion that John eats
    eaten_weight = 0.8 * remaining_weight

    result = eaten_weight
    return result

print(solution())