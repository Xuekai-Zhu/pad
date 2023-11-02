def solution():
    """Tom rents a helicopter for 2 hours a day for 3 days.  It cost $75 an hour to rent.  How much did he pay?"""
    # Define the hourly rental cost
    HOURLY_COST = 75

    # Define the number of rental days and hours
    rental_days = 3
    rental_hours = 2 * rental_days

    # Calculate the total rental cost
    total_cost = HOURLY_COST * rental_hours

    # Display the total rental cost
    result = total_cost
    return result

print(solution())