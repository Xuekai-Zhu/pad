def solution():
    # Calculate the current travel time of Kevin
    current_time = 600 / 50  # distance / rate = time

    # Calculate the desired travel time of Kevin
    desired_time = current_time - 4

    # Calculate the required rate to achieve the desired travel time
    required_rate = 600 / desired_time

    # Calculate how much faster Kevin must travel
    faster_speed = required_rate - 50

    result = faster_speed
    return result

print(solution())