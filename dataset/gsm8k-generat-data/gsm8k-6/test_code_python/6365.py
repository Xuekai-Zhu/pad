def solution():
    # Calculate the time taken by each train to reach their destinations
    time_taken_train1 = 200/50  # time = distance/speed
    time_taken_train2 = 240/80

    # Calculate the average time taken by both trains
    avg_time = (time_taken_train1 + time_taken_train2)/2

    # Round the average time to the nearest integer
    result = round(avg_time)
    return result

print(solution())