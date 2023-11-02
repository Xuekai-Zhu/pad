def solution():
    """The sewers in Middleton can handle 240,000 gallons of run-off. Each hour of rain produces 1000 gallons of runoff. How many days of rain can the sewers handle before they overflow?"""
    # Define the maximum capacity of the sewers
    MAX_CAPACITY = 240000

    # Calculate the amount of runoff produced per day
    runoff_per_day = 24 * 1000

    # Calculate the number of days of rain the sewers can handle before they overflow
    num_days = MAX_CAPACITY // runoff_per_day

    # Display the number of days
    result = num_days
    return result

print(solution())