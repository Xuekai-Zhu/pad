def solution():
    
    jobs_to_complete = 5
    time_per_job = 1  
    men_count = 3
    wage_per_hour = 10
    
    total_time = jobs_to_complete * time_per_job
    total_wage = total_time * men_count * wage_per_hour
    result = total_wage
    return result

print(solution())