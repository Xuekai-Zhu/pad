def solution():
    tylenol_dose = 1000  # Jeremy takes 1000 mg of Tylenol every 6 hours
    dosage_interval = 6  # Jeremy takes the Tylenol every 6 hours
    duration_in_days = 14  # Jeremy takes the Tylenol for 2 weeks
    pill_strength = 500  # Each Tylenol pill is 500 mg

    # Calculate the total number of pills Jeremy will take
    total_dose = (tylenol_dose / pill_strength) * dosage_interval * 24 * duration_in_days
    total_pills = total_dose / pill_strength
    result = total_pills
    return result

print(solution())