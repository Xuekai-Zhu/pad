def solution():
    # Define the total distance and the distance remaining after the first 10 miles
    total_distance = 26
    distance_remaining = total_distance - 10

    # Calculate the time it takes to run the first 10 miles
    time_first_10_miles = 1

    # Calculate the speed for the remaining distance
    speed_remaining = 0.8 * (distance_remaining / (total_distance / time_first_10_miles))

    # Calculate the time it takes to run the remaining distance
    time_remaining = distance_remaining / speed_remaining

    # Calculate the total time for the race
    total_time = time_first_10_miles + time_remaining
    result = total_time
    return result

print(solution())