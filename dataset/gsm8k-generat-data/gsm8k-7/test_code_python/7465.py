def solution():
    initial_weight = 120
    muscle_gain = 0.2 * initial_weight
    fat_gain = 0.25 * muscle_gain

    # Calculate James' new weight
    new_weight = initial_weight + muscle_gain + fat_gain
    result = new_weight
    return result

print(solution())