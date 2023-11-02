def solution():
    num_employees = 300  # There are 300 employees in the factory
    num_emp_earning_12 = 200  # 200 employees earn $12 per hour
    num_emp_earning_14 = 40  # 40 employees earn $14 per hour

    # Calculate the cost of paying the employees who earn $12 per hour
    cost_employees_12 = num_emp_earning_12 * 12 * 8

    # Calculate the cost of paying the employees who earn $14 per hour
    cost_employees_14 = num_emp_earning_14 * 14 * 8

    # Calculate the number of employees who earn $17 per hour
    num_emp_earning_17 = num_employees - num_emp_earning_12 - num_emp_earning_14

    # Calculate the cost of paying the employees who earn $17 per hour
    cost_employees_17 = num_emp_earning_17 * 17 * 8

    # Calculate the total cost of employing all these people for one 8-hour shift
    total_cost = cost_employees_12 + cost_employees_14 + cost_employees_17
    result = total_cost
    return result

print(solution())