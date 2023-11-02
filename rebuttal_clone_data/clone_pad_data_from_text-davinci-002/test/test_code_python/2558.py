def solution():
    current_job_hours = 8
    current_job_wage = 10
    new_job_hours = 4
    new_job_wage = 15
    new_job_bonus = 35
    total_new_job_wage = new_job_hours * new_job_wage + new_job_bonus
    total_current_job_wage = current_job_hours * current_job_wage
    difference = total_new_job_wage - total_current_job_wage
    result = difference
    return result

print(solution())