def solution():
    """The car-rental agency charges $30/day for a car, or $190 for the first week for a rental that lasts an entire week or longer. Jennie rented a car for 11 days. How much, in dollars, did she pay for the rental?"""
    rental_days = 11
    weekly_rate = 190
    daily_rate = 30
    if rental_days >= 7:
        total_cost = weekly_rate + ((rental_days - 7) * daily_rate)
    else:
        total_cost = rental_days * daily_rate
    result = total_cost
    return result

print(solution())