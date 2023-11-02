def solution():
    # Calculate the time for the first train to complete its journey
    time_first_train = 200 / 50  # Distance / Speed

    # Calculate the time for the second train to complete its journey
    time_second_train = 240 / 80  # Distance / Speed

    # Calculate the average time for both trains
    average_time = (time_first_train + time_second_train) / 2

    # Round the average time to the nearest integer
    result = round(average_time)

    return result

print(solution())