def solution():
    
    starting_point = 0
    back_steps = 5 + 2
    forward_steps = 10 + (2 * 2)
    total_steps = forward_steps - back_steps
    result = total_steps
    return result

print(solution())