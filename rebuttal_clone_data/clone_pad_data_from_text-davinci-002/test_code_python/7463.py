def solution():
    initial_workers = 90
    men = (2/3) * initial_workers
    women = initial_workers - men
    new_employees = 10
    total_employees = initial_workers + new_employees
    percentage_of_women = (women / total_employees) * 100
    result = percentage_of_women
    return result

print(solution())