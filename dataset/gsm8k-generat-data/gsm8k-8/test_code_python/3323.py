def solution():
    total_distance = 10

    # Calculate the time it takes to push the car for the first 3 miles
    time_1 = 3 / 6

    # Calculate the time it takes to push the car for the next 3 miles
    time_2 = 3 / 3

    # Calculate the time it takes to push the car for the last 4 miles
    time_3 = 4 / 8

    # Calculate the total time it takes to push the car back to town
    total_time = time_1 + time_2 + time_3
    result = total_time
    return result

print(solution())