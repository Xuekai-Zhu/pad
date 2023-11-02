def solution():
    worker_salary = 100  # Each construction worker makes $100/day
    electrician_salary = 2 * worker_salary  # The electrician makes double the worker's salary
    plumber_salary = 2.5 * worker_salary  # The plumber makes 250% of the worker's salary

    # Calculate the total labor costs for one day
    total_labor_costs = 2 * worker_salary + electrician_salary + plumber_salary
    result = total_labor_costs
    return result

print(solution())