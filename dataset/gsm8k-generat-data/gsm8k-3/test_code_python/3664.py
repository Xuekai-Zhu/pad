def solution():
    """Bob's school track is 400 meters. If Bob ran the first lap in 70 seconds, the second and third lap in 85 seconds each, what was his average speed in (m/s) for his entire run?"""
    # Define the distance of Bob's run and the time for each lap
    distance = 400
    time1 = 70
    time2 = 85
    time3 = 85

    # Calculate the total time for the entire run
    total_time = time1 + time2 + time3

    # Calculate the average speed in m/s
    speed = distance / (total_time / 3)

    # Display the average speed
    result = speed
    return result

print(solution())