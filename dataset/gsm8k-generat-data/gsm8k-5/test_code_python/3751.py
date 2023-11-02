def solution():
    monkey_speed = 1.2  # Monkey swings at an average distance of 1.2 meters per second
    time_in_minutes = 30  # Monkey swings for 30 minutes
    time_in_seconds = time_in_minutes * 60  # Convert minutes to seconds

    # Calculate the distance the monkey swings in meters
    distance = monkey_speed * time_in_seconds
    result = distance
    return result

print(solution())