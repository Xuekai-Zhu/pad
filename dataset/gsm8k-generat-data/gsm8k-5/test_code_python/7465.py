def solution():
    current_weight = 120  # James currently weighs 120 kg

    # Calculate the weight gained from muscle
    muscle_weight = current_weight * 0.2

    # Calculate the weight gained from fat
    fat_weight = muscle_weight / 4

    # Calculate the total weight gained
    total_weight_gain = muscle_weight + fat_weight

    # Calculate James' new weight
    new_weight = current_weight + total_weight_gain
    result = new_weight
    return result

print(solution())