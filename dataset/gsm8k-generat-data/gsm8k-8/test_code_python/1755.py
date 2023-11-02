def solution():
    # Define the variables
    normal_distance = 150
    normal_time = 3
    extra_distance = 50

    # Calculate the new total distance and time
    total_distance = normal_distance + (2 * extra_distance)
    total_time = normal_time + (2 * (extra_distance / normal_time))

    result = total_time
    return result

print(solution())