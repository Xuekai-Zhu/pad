def solution():
    # Calculate the teacher's new salary after the 20% raise
    new_salary = 45000 * 1.2

    # Calculate the total cost for the teacher's salary for one year
    total_cost = new_salary / 9

    # Calculate the cost per parent per year
    cost_per_parent = total_cost / 2

    result = cost_per_parent
    return result

print(solution())