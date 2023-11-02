def solution():
    hourly_rate = 20  # Doris earns $20 per hour by babysitting
    weekly_hours = (3 * 5) + 5  # Doris babysits for 3 hours every weekday and 5 hours on a Saturday
    monthly_expenses = 1200  # Doris needs to earn at least $1200 for her monthly expenses

    # Calculate how many weeks it takes for Doris to earn enough to cover her monthly expenses
    weeks = monthly_expenses / (weekly_hours * hourly_rate)
    result = weeks
    return result

print(solution())