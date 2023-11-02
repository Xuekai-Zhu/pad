def solution():
    """Two trains left the station at the same time, but took different tracks to their destination. One took a track that was 200 miles long and it went 50 MPH. The other took the other track that was 240 miles long and it went 80 MPH. How much time did it take them on average? (Round to the nearest integer.)"""
    distance_train1 = 200
    speed_train1 = 50
    time_train1 = distance_train1 / speed_train1
    distance_train2 = 240
    speed_train2 = 80
    time_train2 = distance_train2 / speed_train2
    average_time = (time_train1 + time_train2) / 2
    result = round(average_time)
    return result

print(solution())