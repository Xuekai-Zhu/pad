def solution():
    num_indian_days = 3 * 7  # 3 times a week for 7 days
    num_mexican_days = 2 * 7  # 2 times a week for 7 days
    num_other_days = 30 - num_indian_days - num_mexican_days  # assume 30 days in a month

    indian_antacids_per_day = 3
    mexican_antacids_per_day = 2
    other_antacids_per_day = 1

    # Calculate the total antacids taken for each type of food
    total_indian_antacids = num_indian_days * indian_antacids_per_day
    total_mexican_antacids = num_mexican_days * mexican_antacids_per_day
    total_other_antacids = num_other_days * other_antacids_per_day

    # Calculate the total number of antacids taken per month
    total_antacids = total_indian_antacids + total_mexican_antacids + total_other_antacids
    result = total_antacids
    return result

print(solution())