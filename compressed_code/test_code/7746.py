def solution():
    
    total_wages = 160
    hours_worked_second_job = 12
    wage_per_hour_second_job = 9
    total_wages_second_job = hours_worked_second_job * wage_per_hour_second_job
    wages_from_first_job = total_wages - total_wages_second_job
    result = wages_from_first_job
    return result

print(solution())