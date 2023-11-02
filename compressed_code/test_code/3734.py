def solution():
    
    first_step_time = 30
    second_step_time = first_step_time / 2
    third_step_time = (first_step_time + second_step_time)
    total_learning_time = first_step_time + second_step_time + third_step_time
    result = total_learning_time
    return result

print(solution())