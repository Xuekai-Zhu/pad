def solution():
    """Two trains left the station at the same time, but took different tracks to their destination. One took a track that was 200 miles long and it went 50 MPH. The other took the other track that was 240 miles long and it went 80 MPH. How much time did it take them on average? (Round to the nearest integer.)"""
    # Calculate the time it took for the first train to reach its destination
    time1 = 200 / 50

    # Calculate the time it took for the second train to reach its destination
    time2 = 240 / 80

    # Calculate the average time
    average_time = (time1 + time2) / 2

    # Round the average time to the nearest integer
    rounded_time = round(average_time)

    # Display the rounded average time
    result = rounded_time
    return result

print(solution())