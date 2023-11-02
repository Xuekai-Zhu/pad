def solution():
    """Two trains left the station at the same time, but took different tracks to their destination. One took a track that was 200 miles long and it went 50 MPH. The other took the other track that was 240 miles long and it went 80 MPH. How much time did it take them on average? (Round to the nearest integer.)"""
    # Define the distance and speed of the first train
    distance_1 = 200
    speed_1 = 50

    # Define the distance and speed of the second train
    distance_2 = 240
    speed_2 = 80

    # Calculate the time it took for the first train to reach its destination
    time_1 = distance_1 / speed_1

    # Calculate the time it took for the second train to reach its destination
    time_2 = distance_2 / speed_2

    # Calculate the average time it took for both trains to reach their destination
    average_time = (time_1 + time_2) / 2

    # Round the average time to the nearest integer
    result = round(average_time)
    return result

print(solution())