def solution():
    ship_speed = 10  # Tom's ship can travel at 10 miles per hour
    sail_time = 1.5  # Tom is sailing from 1 to 4 PM
    travel_speed = 6  # Tom's ship travels back at a rate of 6 mph

    # Calculate the time it takes Tom to get back
    time_to_get_back = (ship_speed - sail_time) / travel_speed
    result = time_to_get_back
    return result

print(solution())