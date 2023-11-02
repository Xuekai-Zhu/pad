def solution():
    
    total_training_time = 5 * 60  
    multiplication_time = 10
    division_time = 20
    total_problem_time = multiplication_time + division_time
    training_days = total_training_time // total_problem_time
    result = training_days
    return result

print(solution())