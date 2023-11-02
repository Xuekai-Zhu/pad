def solution():
    # Define initial weight
    weight = 120

    # Calculate muscle gain
    muscle_gain = 0.2 * weight

    # Calculate fat gain
    fat_gain = 0.25 * muscle_gain

    # Calculate total weight gain
    total_gain = muscle_gain + fat_gain

    # Calculate new weight
    new_weight = weight + total_gain
    result = new_weight
    return result

print(solution())