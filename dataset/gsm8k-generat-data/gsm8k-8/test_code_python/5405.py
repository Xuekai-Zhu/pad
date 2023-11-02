def solution():
    # Calculate the total time in minutes
    total_time = 5 * 60
    
    # Calculate the time needed for each set of problems
    multiplication_time = 10
    division_time = 20
    
    # Calculate the total time needed for each set of problems
    total_multiplication_time = multiplication_time * 7
    total_division_time = division_time * 7
    
    # Calculate the total time needed for a day of training
    total_daily_time = total_multiplication_time + total_division_time
    
    # Calculate the number of days needed to complete the training
    num_days = total_time // total_daily_time
    
    result = num_days
    return result

print(solution())