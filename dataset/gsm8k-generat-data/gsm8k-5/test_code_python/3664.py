def solution():
    lap1_time = 70  # Bob ran the first lap in 70 seconds
    lap2_time = 85  # Bob ran the second lap in 85 seconds
    lap3_time = 85  # Bob ran the third lap in 85 seconds
    total_distance = 400 * 3  # Bob ran a total distance of 400 meters for each of the 3 laps

    # Calculate the total time taken by Bob to complete the run
    total_time = lap1_time + lap2_time + lap3_time

    # Calculate the average speed of Bob's entire run in m/s
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())