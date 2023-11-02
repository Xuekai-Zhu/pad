def solution():
    # Calculate the amount of muscle gained by James
    muscle_gain = 0.2 * 120  # 20% of his body weight

    # Calculate the amount of fat gained by James
    fat_gain = 0.25 * muscle_gain  # 1/4 of the amount of muscle gained

    # Calculate the total weight gained by James
    total_gain = muscle_gain + fat_gain

    # Calculate James' new weight
    new_weight = 120 + total_gain

    result = new_weight
    return result

print(solution())