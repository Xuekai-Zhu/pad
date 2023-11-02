def solution():
    
    former_salary = 45000
    raise_percentage = 0.2
    new_salary = former_salary * (1 + raise_percentage)
    num_parents = 9
    total_cost = new_salary / num_parents
    result = total_cost
    return result

print(solution())