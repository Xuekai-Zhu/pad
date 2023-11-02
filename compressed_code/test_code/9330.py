def solution():
    
    current_job_hours = 8
    current_job_wage = 10
    current_job_pay = current_job_hours * current_job_wage
    
    new_job_hours = 4
    new_job_wage = 15
    new_job_pay = new_job_hours * new_job_wage
    
    bonus = 35
    
    total_new_pay = new_job_pay + bonus
    
    more_money = total_new_pay - current_job_pay
    
    result = more_money
    
    return result

print(solution())