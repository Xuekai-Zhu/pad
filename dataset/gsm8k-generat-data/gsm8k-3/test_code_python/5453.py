def solution():
    """It takes Bryan 5 minutes to walk from his house to the bus station. Then he rides the bus for 20 minutes. After that, he walks 5 minutes from the bus station to his job. It takes the same amount of time in the morning and the evening. How many hours per year does Bryan spend traveling to and from work, if he works every day?"""
    # Define the time it takes to walk and ride the bus
    WALK_TIME = 5 #minutes
    BUS_TIME = 20 #minutes

    # Define the time it takes to walk from the bus stop to work
    WORK_WALK_TIME = 5 #minutes

    # Define the number of minutes Bryan spends traveling to and from work each day
    daily_travel_time = (2 * WALK_TIME) + BUS_TIME + WORK_WALK_TIME #minutes

    # Calculate the number of minutes Bryan spends traveling to and from work each year
    ANNUAL_TRAVEL_TIME = daily_travel_time * 365 #minutes

    # Convert the annual travel time from minutes to hours
    ANNUAL_TRAVEL_TIME_HOURS = ANNUAL_TRAVEL_TIME / 60 #hours

    # Display the annual travel time
    result = ANNUAL_TRAVEL_TIME_HOURS
    return result

print(solution())