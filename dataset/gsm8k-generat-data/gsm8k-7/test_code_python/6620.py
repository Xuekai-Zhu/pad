def solution():
    hourly_wage = 10
    hours_per_day = 10
    num_days_per_week = 5
    num_weeks = 4

    # Calculate the total earnings of each employee per week
    weekly_earnings = hourly_wage * hours_per_day * num_days_per_week

    # Calculate the savings of each employee per week
    robby_savings = weekly_earnings * (2/5)
    jaylene_savings = weekly_earnings * (3/5)
    miranda_savings = weekly_earnings * (1/2)

    # Calculate the total savings of all employees after four weeks
    total_savings = (robby_savings + jaylene_savings + miranda_savings) * num_weeks
    result = total_savings
    return result

print(solution())