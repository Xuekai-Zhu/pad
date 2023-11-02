def solution():
    # Calculate the time it takes for Jim to catch up to Bob (in hours)
    distance = 1  # Bob has a 1 mile head-start
    relative_speed = 9 - 6  # Jim's relative speed to Bob
    time_in_hours = distance / relative_speed

    # Convert the time to minutes
    time_in_minutes = time_in_hours * 60
    result = time_in_minutes
    return result

print(solution())