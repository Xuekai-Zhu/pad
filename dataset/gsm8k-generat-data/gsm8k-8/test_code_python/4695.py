def solution():
    # Calculate the number of antacids per day for each type of food
    indian_antacids_per_day = 3
    mexican_antacids_per_day = 2
    other_antacids_per_day = 1

    # Calculate the total number of antacids per week
    indian_antacids_per_week = indian_antacids_per_day * 3
    mexican_antacids_per_week = mexican_antacids_per_day * 2
    other_antacids_per_week = 7 - indian_antacids_per_week - mexican_antacids_per_week

    # Calculate the total number of antacids per month
    total_antacids_per_month = (indian_antacids_per_week * 4) + (mexican_antacids_per_week * 4) + (other_antacids_per_week * 4)
    result = total_antacids_per_month
    return result

print(solution())