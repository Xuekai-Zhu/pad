def solution():
    # Define the daily salary of each worker
    worker_salary = 100
    electrician_salary = 2 * worker_salary
    plumber_salary = 2.5 * worker_salary

    # Calculate the total labor costs for one day
    total_labor_costs = 2 * (worker_salary + worker_salary) + electrician_salary + plumber_salary
    result = total_labor_costs
    return result

print(solution())