def solution():
    # Calculate the current travel time
    current_time = 600 / 50

    # Calculate the new travel time with a 4-hour decrease
    new_time = current_time - 4

    # Calculate the new speed required
    new_speed = 600 / new_time - 50
    result = new_speed
    return result

print(solution())