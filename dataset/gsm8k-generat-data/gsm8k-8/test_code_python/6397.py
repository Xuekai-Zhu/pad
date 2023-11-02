def solution():
    # Calculate the cost of the first employee
    employee1_cost = 20 * 40

    # Calculate the cost of the second employee, including the subsidy
    employee2_cost = (22-6) * 40

    # Calculate the difference in cost per week
    cost_difference = employee1_cost - employee2_cost

    result = cost_difference
    return result

print(solution())