def solution():
    
    matt_speed = 20
    tom_speed = matt_speed + 5
    matt_steps = 220
    time_to_reach = matt_steps / matt_speed
    tom_steps = tom_speed * time_to_reach
    result = tom_steps
    return result

print(solution())