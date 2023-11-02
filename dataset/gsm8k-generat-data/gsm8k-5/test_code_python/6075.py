def solution():
    hourly_rate = 20  # Each bodyguard charges $20 an hour
    hours_per_day = 8  # Tim hires them for 8 hours per day
    days_per_week = 7  # Tim hires them for 7 days per week

    # Calculate the total cost per bodyguard per week
    cost_per_week = hourly_rate * hours_per_day * days_per_week

    # Calculate the total cost for both bodyguards per week
    total_cost = cost_per_week * 2

    result = total_cost
    return result

print(solution())