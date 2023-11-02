def solution():
    # Calculate the time it took for the first train to reach its destination
    time_train1 = 200 / 50

    # Calculate the time it took for the second train to reach its destination
    time_train2 = 240 / 80

    # Calculate the average time for both trains
    average_time = (time_train1 + time_train2) / 2

    # Round the average time to the nearest integer
    result = round(average_time)
    return result

print(solution())