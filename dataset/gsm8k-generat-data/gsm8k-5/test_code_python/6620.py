def solution():
    hourly_salary = 10  # Each employee earns $10 per hour
    daily_salary = hourly_salary * 10  # Each employee earns $100 per day
    weekly_salary = daily_salary * 5  # Each employee earns $500 per week
    four_week_salary = weekly_salary * 4  # Each employee earns $2000 in 4 weeks

    # Calculate each employee's savings in 4 weeks
    robby_savings = (2/5) * four_week_salary
    jaylene_savings = (3/5) * four_week_salary
    miranda_savings = 0.5 * four_week_salary

    # Calculate the combined savings of the three employees
    total_savings = robby_savings + jaylene_savings + miranda_savings
    result = total_savings
    return result

print(solution())