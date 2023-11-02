def solution():
    """A big box store sees 175 people enter their store every hour. This number doubles during the holiday season. During the holiday season, how many customers will this big box store see in 8 hours?"""
    regular_customers_per_hour = 175
    holiday_customers_per_hour = regular_customers_per_hour * 2
    hours_during_holiday_season = 8
    total_holiday_customers = holiday_customers_per_hour * hours_during_holiday_season
    result = total_holiday_customers
    return result

print(solution())