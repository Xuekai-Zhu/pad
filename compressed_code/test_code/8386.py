def solution():
    
    worker_salary = 100
    electrician_salary = worker_salary * 2
    plumber_salary = worker_salary * 2.5
    total_labor_cost = (2 * worker_salary) + electrician_salary + plumber_salary
    result = total_labor_cost
    return result

print(solution())