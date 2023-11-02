def solution():
    former_salary = 45000
    raise_percent = 0.2  # 20% raise
    num_parents = 9

    # Calculate the new salary with the 20% raise
    new_salary = former_salary * (1 + raise_percent)

    # Calculate the total cost of the teacher's salary for one year
    total_salary_cost = new_salary * num_parents

    # Calculate the cost per parent
    cost_per_parent = total_salary_cost / num_parents
    result = cost_per_parent
    return result

print(solution())