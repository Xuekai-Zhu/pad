def solution():
    
    total_operation_cost = 4000
    emp_salaries = total_operation_cost * 2/5
    remaining_cost = total_operation_cost - emp_salaries
    delivery_cost = remaining_cost * 1/4
    total_other_expenses = emp_salaries + delivery_cost
    orders_cost = total_operation_cost - total_other_expenses
    result = orders_cost
    return result

print(solution())