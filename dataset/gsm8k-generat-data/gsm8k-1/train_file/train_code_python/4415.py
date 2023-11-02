def solution():
    """The car-rental agency charges $30/day for a car, or $190 for the first week for a rental that lasts an entire week or longer. Jennie rented a car for 11 days. How much, in dollars, did she pay for the rental?"""
    rental_length = 11
    weekly_rate = 190
    daily_rate = 30
    if rental_length >= 7:
        total_cost = weekly_rate + daily_rate * (rental_length - 7)
    else:
        total_cost = daily_rate * rental_length
    result = total_cost
    return result

print(solution())