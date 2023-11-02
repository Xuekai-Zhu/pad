def solution():
    
    total_wages = 160
    second_job_pay = 9
    second_job_hours = 12
    second_job_wages = second_job_pay * second_job_hours
    first_job_wages = total_wages - second_job_wages
    result = first_job_wages
    return result

print(solution())