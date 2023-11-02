def solution():
    """Two trains left the station at the same time, but took different tracks to their destination. One took a track that was 200 miles long and it went 50 MPH. The other took the other track that was 240 miles long and it went 80 MPH. How much time did it take them on average? (Round to the nearest integer.)"""
    distance_1 = 200
    speed_1 = 50
    time_1 = distance_1 / speed_1
    distance_2 = 240
    speed_2 = 80
    time_2 = distance_2 / speed_2
    average_time = (time_1 + time_2) / 2
    result = round(average_time)
    return result

print(solution())