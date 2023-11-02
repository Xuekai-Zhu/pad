def solution():
    """A big box store sees 175 people enter their store every hour.  This number doubles during the holiday season.  During the holiday season, how many customers will this big box store see in 8 hours?"""
    # Define the number of customers entering the store during non-holiday season
    non_holiday_customers = 175

    # Define the number of hours the store is open during holiday season
    holiday_hours = 8

    # Calculate the number of customers entering the store during holiday season
    holiday_customers = non_holiday_customers * 2

    # Calculate the total number of customers during holiday season
    total_customers = holiday_customers * holiday_hours

    # Display the total number of customers
    result = total_customers
    return result

print(solution())