def solution():
    
    
    first_staircase = 20
    second_staircase = 2 * first_staircase
    third_staircase = second_staircase - 10
    step_length = 0.5
    
    total_steps = first_staircase + second_staircase + third_staircase
    total_feet = total_steps * step_length
    
    result = total_feet
    
    return result

print(solution())