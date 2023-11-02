def solution():
    """Jeremy decides to take Tylenol because of the pain he is experiencing. He decides to take 1000 mg every 6 hours for 2 weeks. How many pills do they take if they are each 500 mg?"""
    dose = 1000
    interval = 6 # in hours
    duration = 14 # in days
    pills_per_dose = dose / 500
    doses_per_day = 24 / interval
    total_doses = doses_per_day * duration
    total_pills = total_doses * pills_per_dose
    result = total_pills
    return result

print(solution())