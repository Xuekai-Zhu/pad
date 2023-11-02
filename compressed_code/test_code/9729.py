def solution():
    
    initial_time = 8
    percent_increase = 75
    new_time = initial_time * (1 + percent_increase / 100)
    initial_speed = 8
    speed_increase = 4
    new_speed = initial_speed + speed_increase
    distance = new_time * new_speed
    result = distance
    return result

print(solution())