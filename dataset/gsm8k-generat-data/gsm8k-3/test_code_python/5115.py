def solution():
    """Janet makes $20 per hour at work. She works 52 hours per week. Anything over 40 hours per week is considered overtime and is paid at 1.5 times the normal rate. She wants to purchase a $4640 car. How many weeks does she need to work to purchase the car?"""
    # Define the hourly rate and the overtime multiplier
    HOURLY_RATE = 20
    OVERTIME_MULTIPLIER = 1.5

    # Define the number of hours worked per week and the weekly earnings
    WEEKLY_HOURS = 52
    WEEKLY_EARNINGS = 40 * HOURLY_RATE + (WEEKLY_HOURS - 40) * HOURLY_RATE * OVERTIME_MULTIPLIER

    # Define the cost of the car and calculate the number of weeks needed to purchase it
    CAR_COST = 4640
    weeks_needed = CAR_COST / WEEKLY_EARNINGS

    # Display the number of weeks needed to purchase the car
    result = weeks_needed
    return result

print(solution())