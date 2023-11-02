def solution():
    time_in_hours = 42 / 60  # convert minutes to hours
    speed = 50  # mph

    # Calculate the distance traveled using the formula: distance = speed * time
    distance_traveled = speed * time_in_hours
    result = distance_traveled
    return result

print(solution())