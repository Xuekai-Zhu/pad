def solution():
    """Latia wants to buy a Samsung TV worth $1700. She works for a delivery service company for a month earning $10 per hour for a 30-hour workweek. How many more hours does she have to work to buy the TV?"""
    tv_cost = 1700
    weekly_hours = 30
    hourly_rate = 10
    monthly_income = weekly_hours * hourly_rate * 4
    extra_income_needed = tv_cost - monthly_income
    hours_needed = extra_income_needed / hourly_rate
    result = hours_needed
    return result

print(solution())