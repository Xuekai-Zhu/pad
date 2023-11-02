def solution():
    
    unicorns = 6
    flowers_per_step = 4
    distance = 9000  
    step_length = 3
    steps = distance // step_length
    total_flowers = unicorns * steps * flowers_per_step
    result = total_flowers
    return result

print(solution())