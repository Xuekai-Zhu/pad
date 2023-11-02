def solution():
    initial_salary = 45000
    raise_percentage = 20
    raise_amount = initial_salary * (raise_percentage / 100)
    new_salary = initial_salary + raise_amount
    children = 9
    total_cost = new_salary * children
    cost_per_parent = total_cost / children
    result = cost_per_parent
    
    return result

print(solution())