def solution():
    # Calculate time for first part of journey with loaded sled
    distance1 = 180
    speed1 = 10
    time1 = distance1/speed1

    # Calculate time for second part of journey with unloaded sled
    distance2 = 120
    speed2 = 20
    time2 = distance2/speed2

    # Calculate time for third part of journey with loaded sled
    distance3 = 80
    speed3 = 10
    time3 = distance3/speed3

    # Calculate time for fourth part of journey with unloaded sled
    distance4 = 140
    speed4 = 20
    time4 = distance4/speed4

    # Calculate total time spent pulling sled
    total_time = time1 + time2 + time3 + time4
    result = total_time
    
    return result

print(solution())