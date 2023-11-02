def solution():
    # Calculate the total cost of the first group of employees
    group1_cost = 200 * 12 * 8

    # Calculate the total cost of the second group of employees
    group2_cost = 40 * 14 * 8

    # Calculate the number of employees in the third group
    group3_employees = 300 - 200 - 40

    # Calculate the total cost of the third group of employees
    group3_cost = group3_employees * 17 * 8

    # Calculate the total cost of employing all 300 employees for one 8-hour shift
    total_cost = group1_cost + group2_cost + group3_cost
    result = total_cost
    return result

print(solution())