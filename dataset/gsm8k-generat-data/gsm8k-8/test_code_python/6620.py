def solution():
    # Define the variables
    hourly_rate = 10
    hours_per_day = 10
    work_days_per_week = 5
    weeks = 4

    # Calculate the total earnings of each employee per week
    weekly_earnings = hourly_rate * hours_per_day * work_days_per_week

    # Calculate the savings of each employee per week
    robby_savings = weekly_earnings * 2/5
    jaylene_savings = weekly_earnings * 3/5
    miranda_savings = weekly_earnings * 1/2

    # Calculate the combined savings of the three employees after four weeks
    combined_savings = (robby_savings + jaylene_savings + miranda_savings) * weeks
    result = combined_savings
    return result

print(solution())