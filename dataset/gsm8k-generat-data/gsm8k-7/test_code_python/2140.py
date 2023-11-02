def solution():
    num_tylenol = 2
    tylenol_dosage = 375
    num_hours_day = 24

    # Calculate the number of Tylenol tablets James takes in a day
    num_tylenol_day = num_hours_day / 6 * num_tylenol

    # Calculate the total dosage James takes in a day
    total_dosage = num_tylenol_day * tylenol_dosage
    result = total_dosage
    return result

print(solution())