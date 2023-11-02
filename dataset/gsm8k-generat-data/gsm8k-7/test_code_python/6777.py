def solution():
    total_time = 8
    speed1 = 70
    speed2 = 85

    # Calculate the time spent traveling at speed1 and speed2
    time1 = total_time / 2
    time2 = total_time / 2

    # Calculate the distance traveled at speed1 and speed2
    distance1 = speed1 * time1
    distance2 = speed2 * time2

    # Calculate the total distance traveled
    total_distance = distance1 + distance2
    result = total_distance
    return result

print(solution())