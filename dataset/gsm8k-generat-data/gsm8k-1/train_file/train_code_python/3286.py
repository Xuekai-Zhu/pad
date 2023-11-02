def solution():
    """Jason is hiring two construction workers, one electrician and one plumber. If the construction workers each make $100/day, the electrician makes double what a worker is paid and the plumber makes 250% of a worker's salary, how much are the overall labor costs for one day?"""
    worker_salary = 100
    electrician_salary = worker_salary * 2
    plumber_salary = worker_salary * 2.5
    total_labor_cost = (2 * worker_salary) + electrician_salary + plumber_salary
    result = total_labor_cost
    return result

print(solution())