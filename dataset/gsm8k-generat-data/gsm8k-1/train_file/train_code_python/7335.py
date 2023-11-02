def solution():
    """Damien jogs 5 miles per day on weekdays only. How many miles does he run over three weeks?"""
    miles_per_day = 5
    weekdays_per_week = 5
    weeks = 3
    total_miles = miles_per_day * weekdays_per_week * weeks
    result = total_miles
    return result

print(solution())