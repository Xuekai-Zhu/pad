def solution():
    tylenol_dosage = 2 * 375  # James takes 2 Tylenol tablets that are 375 mg each
    dosage_interval = 6  # James takes the dosage every 6 hours
    hours_in_a_day = 24  # There are 24 hours in a day

    # Calculate the total dosage James takes in a day
    total_daily_dosage = tylenol_dosage * (hours_in_a_day / dosage_interval)
    result = total_daily_dosage
    return result

print(solution())