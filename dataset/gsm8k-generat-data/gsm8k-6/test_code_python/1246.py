def solution():
    # Total number of hours in 3 days
    total_hours = 3 * 24

    # Calculate the total hours the spaceship spent moving
    moving_hours = 10 + 10 + ((total_hours - 24) // 11) * 10  # traveled for 10 hours twice, then traveled for 10 hours every 11 hours

    # Calculate the total hours the spaceship was stopped
    stopped_hours = 3 + 1 + ((total_hours - 24) // 11) * 1  # stopped for 3 hours once, then stopped for 1 hour every 11 hours

    # Calculate the total hours the spaceship was not moving
    not_moving_hours = total_hours - moving_hours - stopped_hours
    result = not_moving_hours
    return result

print(solution())