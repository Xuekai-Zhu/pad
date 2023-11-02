def solution():
    
    distance = 600
    initial_speed = 50
    initial_time = distance / initial_speed
    decrease_in_time = 4
    new_time = initial_time - decrease_in_time
    new_speed = distance / new_time
    increase_in_speed = new_speed - initial_speed
    result = increase_in_speed
    return result

print(solution())