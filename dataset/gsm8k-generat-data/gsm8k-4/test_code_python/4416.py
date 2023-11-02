def solution():
    """The car-rental agency charges $30/day for a car, or $190 for the first week for a rental that lasts an entire week or longer. Jennie rented a car for 11 days. How much, in dollars, did she pay for the rental?"""
    # Define the daily rental price and the weekly rental price
    DAILY_PRICE = 30
    WEEKLY_PRICE = 190

    # Calculate the number of weeks and days in the rental period
    weeks = 11 // 7
    days = 11 % 7

    # Calculate the rental cost
    if weeks >= 1:
        rental_cost = WEEKLY_PRICE * weeks
        if days > 0:
            rental_cost += days * DAILY_PRICE
    else:
        rental_cost = days * DAILY_PRICE

    # return the result
    result = rental_cost
    return result

print(solution())