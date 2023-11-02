def solution():
    
    total_cost = 4000
    employee_salary = total_cost * (2/5)
    remaining_cost = total_cost - employee_salary
    delivery_cost = remaining_cost * (1/4)
    order_cost = remaining_cost - delivery_cost
    result = order_cost
    return result

print(solution())