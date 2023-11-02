def solution():
    # Calculate the amount of protein Matt needs per day
    protein_per_day = 2 * 80  # 2 grams of protein per kilogram of body weight

    # Calculate the amount of protein powder Matt needs to eat per day
    protein_powder_per_day = protein_per_day / 0.8  # 80% of protein powder is protein

    # Calculate the amount of protein powder Matt needs to eat per week
    protein_powder_per_week = protein_powder_per_day * 7

    result = protein_powder_per_week
    return result

print(solution())