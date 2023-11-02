def solution():
    tylenol_per_dose = 1000  # Mark takes 2 Tylenol tablets of 500 mg each
    doses_per_day = 3  # Mark takes Tylenol every 4 hours for 12 hours
    total_tylenol = tylenol_per_dose * doses_per_day  # Calculate the total Tylenol per day in milligrams

    # Convert the total Tylenol per day to grams
    total_tylenol_grams = total_tylenol / 1000
    result = total_tylenol_grams
    return result

print(solution())