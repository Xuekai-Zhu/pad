def solution():
    """Latia wants to buy a Samsung TV worth $1700. She works for a delivery service company for a month earning $10 per hour for a 30-hour workweek. How many more hours does she have to work to buy the TV?"""
    # Define the cost of the TV and Latia's hourly wage
    TV_COST = 1700
    HOURLY_WAGE = 10

    # Calculate Latia's earnings for one week
    weekly_earnings = HOURLY_WAGE * 30

    # Calculate the number of weeks it would take Latia to earn enough to buy the TV
    weeks_to_save = TV_COST / weekly_earnings

    # Calculate the number of hours Latia would need to work to earn enough to buy the TV
    hours_to_save = weeks_to_save * 30

    # Display the number of hours Latia would need to work
    result = hours_to_save
    return result

print(solution())