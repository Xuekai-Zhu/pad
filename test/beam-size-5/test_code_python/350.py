def solution():
    
    phone_cost = 400
    savings = 80
    first_job_pay = 10 * 20
    second_job_pay = 5 * 15
    total_pay = first_job_pay + second_job_pay
    remaining_savings = phone_cost - total_pay
    result = remaining_savings
    return result

print(solution())