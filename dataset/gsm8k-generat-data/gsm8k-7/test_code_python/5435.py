def solution():
    protein_percentage = 0.8
    body_weight = 80
    protein_per_kg = 2
    days_per_week = 7

    # Calculate the total protein Matt needs per day
    total_protein_per_day = body_weight * protein_per_kg

    # Calculate the amount of protein powder Matt needs to eat per day
    protein_powder_per_day = total_protein_per_day / protein_percentage

    # Calculate the amount of protein powder Matt needs to eat per week
    protein_powder_per_week = protein_powder_per_day * days_per_week
    result = protein_powder_per_week
    return result

print(solution())