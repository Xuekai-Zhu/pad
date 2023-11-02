def solution():
    """Doris earns $20 per hour by babysitting. She needs to earn at least $1200 for her monthly expenses. She can babysit for 3 hours every weekday and 5 hours on a Saturday. How many weeks does it take for Doris to earn enough to cover her monthly expenses?"""
    hourly_rate = 20
    monthly_expenses = 1200
    weekday_hours = 3 * 5
    saturday_hours = 5
    total_hours_per_week = weekday_hours + saturday_hours
    total_earned_per_week = total_hours_per_week * hourly_rate
    weeks_to_cover_expenses = monthly_expenses / total_earned_per_week
    result = weeks_to_cover_expenses
    return result

print(solution())