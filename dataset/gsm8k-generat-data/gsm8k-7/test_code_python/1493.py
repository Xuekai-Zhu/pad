def solution():
    distance_1 = 100  # miles
    time_1 = 1  # hour
    distance_2 = 300

    # Calculate the speed for the first part of the journey
    speed_1 = distance_1 / time_1

    # Calculate the time it takes to complete the second part of the journey
    time_2 = distance_2 / speed_1

    # Calculate the total time for the trip
    total_time = time_1 + time_2
    result = total_time
    return result

print(solution())