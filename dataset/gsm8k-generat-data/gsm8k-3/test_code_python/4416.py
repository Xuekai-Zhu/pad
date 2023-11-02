def solution():
    """The car-rental agency charges $30/day for a car, or $190 for the first week for a rental that lasts an entire week or longer. Jennie rented a car for 11 days. How much, in dollars, did she pay for the rental?"""
    # Define the daily rental price and the weekly rental price
    DAILY_PRICE = 30
    WEEKLY_PRICE = 190

    # Get the number of days Jennie rented the car
    days_rented = 11

    # Calculate Jennie's rental price
    if days_rented < 7:
        rental_price = days_rented * DAILY_PRICE
    else:
        weeks_rented = days_rented // 7
        extra_days_rented = days_rented % 7
        rental_price = (weeks_rented * WEEKLY_PRICE) + (extra_days_rented * DAILY_PRICE)

    # Display Jennie's rental price
    result = rental_price
    return result

print(solution())