def solution():
    # Calculate the time difference between when Mars disappears and Uranus appears
    time_diff = (2 * 60) + 41 + (3 * 60) + 16

    # Convert the time difference to hours and minutes
    hours, minutes = divmod(time_diff, 60)

    # Add the time difference to 12:10 AM
    uranus_appearance = (12 + hours, 10 + minutes)

    # Convert the uranus_appearance time to minutes since 6:00 AM
    hours_diff = uranus_appearance[0] - 6
    minutes_diff = uranus_appearance[1]

    total_minutes = (hours_diff * 60) + minutes_diff
    result = total_minutes
    return result

print(solution())