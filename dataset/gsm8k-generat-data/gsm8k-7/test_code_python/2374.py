def solution():
    num_employees = 300
    num_emp_12 = 200
    num_emp_14 = 40
    emp_12_pay = 12
    emp_14_pay = 14
    emp_other_pay = 17
    shift_length = 8

    # Calculate the cost of paying the employees who earn $12 per hour
    cost_emp_12 = num_emp_12 * emp_12_pay * shift_length

    # Calculate the cost of paying the employees who earn $14 per hour
    cost_emp_14 = num_emp_14 * emp_14_pay * shift_length

    # Calculate the cost of paying the employees who earn $17 per hour
    cost_emp_other = (num_employees - num_emp_12 - num_emp_14) * emp_other_pay * shift_length

    # Calculate the total cost of employing all the people for one 8-hour shift
    total_cost = cost_emp_12 + cost_emp_14 + cost_emp_other
    result = total_cost
    return result

print(solution())