def solution():
    
    construction_worker_salary = 100
    electrician_salary = 2 * construction_worker_salary
    plumber_salary = 2.5 * construction_worker_salary
    total_labor_cost = 2 * construction_worker_salary + electrician_salary + plumber_salary
    result = total_labor_cost
    return result

print(solution())