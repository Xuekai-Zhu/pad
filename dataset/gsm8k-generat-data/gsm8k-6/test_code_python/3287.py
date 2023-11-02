def solution():
    # Calculate the daily wage of a construction worker
    worker_wage = 100  

    # Calculate the daily wage of the electrician
    electrician_wage = worker_wage * 2  

    # Calculate the daily wage of the plumber
    plumber_wage = worker_wage * 2.5  

    # Calculate the total cost of labor for one day
    total_cost = (2 * worker_wage) + electrician_wage + plumber_wage  
    result = total_cost
    return result

print(solution())