def solution():
    worker_pay = 100
    electrician_pay = 2 * worker_pay
    plumber_pay = 2.5 * worker_pay

    # Calculate the total labor cost for one day
    total_labor_cost = (2 * worker_pay) + electrician_pay + plumber_pay
    result = total_labor_cost
    return result

print(solution())