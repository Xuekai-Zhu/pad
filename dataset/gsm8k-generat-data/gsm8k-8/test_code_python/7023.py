def solution():
    # Calculate the total distance Iggy runs
    total_distance = 3 + 4 + 6 + 8 + 3

    # Convert the total distance to miles
    total_distance_in_miles = total_distance / 1

    # Calculate the total time Iggy spends running in minutes
    total_time_in_minutes = total_distance_in_miles * 10

    # Convert the total time to hours
    total_time_in_hours = total_time_in_minutes / 60

    result = total_time_in_hours
    return result

print(solution())