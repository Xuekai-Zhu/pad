def solution():
    
    distance1 = 3
    speed1 = 150
    distance2 = 2
    speed2 = speed1 + 50
    distance3 = 1
    speed3 = speed1 * 2
    total_distance = distance1 + distance2 + distance3
    total_time = (distance1 / speed1) + (distance2 / speed2) + (distance3 / speed3)
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())