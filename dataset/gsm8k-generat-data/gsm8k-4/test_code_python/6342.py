def solution():
    """A big box store sees 175 people enter their store every hour.  This number doubles during the holiday season.  During the holiday season, how many customers will this big box store see in 8 hours?"""
    # Define the number of customers per hour and the number of holiday hours
    customers_per_hour = 175
    holiday_hours = 8

    # Double the number of customers per hour during the holiday season
    holiday_customers_per_hour = customers_per_hour * 2

    # Calculate the total number of customers during the holiday season
    total_customers = holiday_customers_per_hour * holiday_hours

    # Return the result
    result = total_customers
    return result

print(solution())