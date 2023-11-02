def solution():
    # Calculate the amount of protein Matt needs per day
    protein_per_day = 2 * 80 * 0.8  # 2 g per kg of body weight, 80 kg, 80% protein powder

    # Calculate the amount of protein Matt needs per week
    protein_per_week = protein_per_day * 7

    # Convert the amount of protein to the amount of protein powder needed per week
    powder_per_week = protein_per_week / 0.8  # 80% protein powder

    result = powder_per_week
    return result

print(solution())