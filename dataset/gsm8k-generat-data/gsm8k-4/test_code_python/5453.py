def solution():
    """It takes Bryan 5 minutes to walk from his house to the bus station. Then he rides the bus for 20 minutes. After that, he walks 5 minutes from the bus station to his job. It takes the same amount of time in the morning and the evening. How many hours per year does Bryan spend traveling to and from work, if he works every day?"""
    # Define the time it takes to walk, ride the bus, and walk again
    WALK_TIME = 5
    BUS_TIME = 20

    # Calculate the total travel time for a round trip
    round_trip_time = (2 * WALK_TIME) + BUS_TIME

    # Calculate the total travel time per day
    daily_travel_time = round_trip_time * 2

    # Calculate the total travel time per year
    yearly_travel_time = daily_travel_time * 365 / 60

    # return the result in hours
    result = yearly_travel_time
    return result

print(solution())