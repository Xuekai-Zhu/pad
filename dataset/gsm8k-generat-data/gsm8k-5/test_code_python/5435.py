def solution():
    protein_percentage = 0.8  # Matt's protein powder is 80% protein
    weight = 80  # Matt weighs 80 kg
    protein_per_kg = 2  # Matt wants to eat 2 grams of protein per kilogram of body weight each day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total amount of protein Matt needs to eat per day
    total_protein_per_day = weight * protein_per_kg

    # Calculate the amount of protein powder Matt needs to eat per day
    protein_powder_per_day = total_protein_per_day / protein_percentage

    # Calculate the amount of protein powder Matt needs to eat per week
    protein_powder_per_week = protein_powder_per_day * days_per_week
    result = protein_powder_per_week
    return result

print(solution())