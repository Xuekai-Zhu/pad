def solution():
    # Convert time to hours
    time_in_hours = 10 / 60

    # Calculate required speed
    required_speed = 5 / time_in_hours

    # Convert to miles per hour
    mph_required = required_speed * 60

    result = mph_required
    return result

print(solution())