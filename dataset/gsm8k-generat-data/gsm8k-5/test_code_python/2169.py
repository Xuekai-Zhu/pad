def solution():
    race_distance = 5  # The race is 5 miles long
    john_speed = 15  # John runs at a speed of 15 mph
    john_time = race_distance / john_speed * 60  # Calculate John's time in minutes

    # Calculate the time of the next fastest guy
    next_fastest_time = 23

    # Calculate the time difference between John and the next fastest guy
    time_difference = john_time - next_fastest_time

    result = time_difference
    return result

print(solution())