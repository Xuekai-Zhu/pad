def solution():
    """Rodney and Todd are rowing down a river that is 50 yards wide at one end. If the river's width increases from this end uniformly by 2 yards every 10 meters along, and they row along the river at a rate of 5 m/s, how long (in seconds) will it take them to get to the point where the river is 80 yards wide?"""
    # Define the initial width and rate of increase of the river
    initial_width = 50
    rate_of_increase = 2  # in yards per 10 meters

    # Define the distance they need to cover and their speed
    total_distance = 30 * 10  # in meters
    speed = 5  # in meters per second

    # Define the time it takes to cross the initial width of the river
    initial_time = initial_width / speed

    # Calculate the final width of the river
    final_width = initial_width + (rate_of_increase * total_distance / 10)

    # Calculate the time it takes to cross the final width of the river
    final_time = final_width / speed

    # Calculate the total time it takes to cross the river
    total_time = initial_time + final_time

    # Return the result in seconds
    result = total_time
    return result

print(solution())