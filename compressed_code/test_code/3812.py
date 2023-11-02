def solution():
    
    total_floors = 9
    steps_per_floor = 30
    total_steps = total_floors * steps_per_floor
    jake_speed = 3
    jake_time = total_steps / jake_speed
    elevator_time = 60
    time_difference = jake_time - elevator_time
    result = time_difference
    return result

print(solution())