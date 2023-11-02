def solution():
    
    distance = 80
    time = 2
    speed = distance / time
    distance_in_quarter_hour = (speed / 60) * 15
    result = distance_in_quarter_hour
    return result

print(solution())