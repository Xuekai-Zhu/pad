def solution():
    # Calculate the total number of hours in 3 days (72 hours)
    total_hours = 72

    # Calculate the total hours the spaceship was moving based on the given pattern
    moving_hours = 20 + 10 * int((total_hours - 24) / 11)

    # Calculate the total hours the spaceship was stopped based on the given pattern
    stopped_hours = 3 + 1 * int((total_hours - 24) / 11) + 2 * int((total_hours - 24) / 11)

    # Calculate the total hours the spaceship was not moving
    not_moving_hours = total_hours - moving_hours - stopped_hours
    result = not_moving_hours
    return result

print(solution())