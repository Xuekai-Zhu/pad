def solution():
    
    distance = 600
    initial_speed = 50
    initial_time = distance / initial_speed
    decreased_time = initial_time - 4
    
    new_speed = distance / decreased_time
    speed_increase = new_speed - initial_speed
    
    result = speed_increase
    return result

print(solution())