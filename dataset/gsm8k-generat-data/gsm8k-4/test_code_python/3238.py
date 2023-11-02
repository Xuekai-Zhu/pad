def solution():
    """Jill can run up a hill at 9 feet/second and down a hill at 12 feet/second. How long does it take her to run up and down a 900 foot hill?"""
    # Define the hill distance and Jill's speed going up and down
    hill_distance = 900
    up_speed = 9
    down_speed = 12

    # Calculate the time it takes Jill to run up the hill and down the hill
    time_up = hill_distance / up_speed
    time_down = hill_distance / down_speed

    # Calculate the total time for the round trip
    total_time = time_up + time_down

    # return the result
    result = total_time
    return result

print(solution())