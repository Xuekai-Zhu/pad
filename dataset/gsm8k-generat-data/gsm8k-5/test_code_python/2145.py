def solution():
    distance_traveled = 5 + 2  # Rudolph traveled 2 more than 5 miles
    stop_signs_encountered = 17 - 3  # Rudolph encountered 3 less than 17 stop signs

    # Calculate the number of stop signs per mile
    stop_signs_per_mile = stop_signs_encountered / distance_traveled
    result = stop_signs_per_mile
    return result

print(solution())