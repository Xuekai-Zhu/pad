def solution():
    """Latia wants to buy a Samsung TV worth $1700. She works for a delivery service company for a month earning $10 per hour for a 30-hour workweek. How many more hours does she have to work to buy the TV?"""
    tv_price = 1700
    hourly_rate = 10
    hours_per_week = 30
    weeks_to_save = tv_price / (hours_per_week * hourly_rate)
    remaining_hours = weeks_to_save * 4 * hours_per_week - 4 * hours_per_week
    result = remaining_hours
    return result

print(solution())