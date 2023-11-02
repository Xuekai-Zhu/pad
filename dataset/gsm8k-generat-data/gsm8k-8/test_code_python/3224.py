def solution():
    # Calculate the time it takes to travel each third of the trip
    time_per_third = 0.25 # 15 minutes is 0.25 hours
    time_first_third = time_per_third
    time_second_third = time_per_third
    time_last_third = time_per_third

    # Calculate the distance traveled during each third of the trip
    distance_first_third = 16 * time_first_third
    distance_second_third = 12 * time_second_third
    distance_last_third = 20 * time_last_third

    # Calculate the total distance traveled
    total_distance = distance_first_third + distance_second_third + distance_last_third

    # Round the total distance to two decimal places and return the result
    result = round(total_distance, 2)
    return result

print(solution())