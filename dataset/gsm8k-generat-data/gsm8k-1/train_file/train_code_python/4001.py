def solution():
    """Jeremy decides to take Tylenol because of the pain he is experiencing. He decides to take 1000 mg every 6 hours for 2 weeks. How many pills do they take if they are each 500 mg?"""
    dosage = 1000
    time_interval = 6 # hours
    num_weeks = 2
    num_days = num_weeks * 7
    num_doses_per_day = 24 / time_interval
    total_doses = num_days * num_doses_per_day
    pills_per_dose = dosage / 500
    total_pills = total_doses * pills_per_dose
    result = total_pills
    return result

print(solution())