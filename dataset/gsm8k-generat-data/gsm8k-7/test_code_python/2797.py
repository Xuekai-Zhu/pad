def solution():
    total_cost = 4000
    emp_salary = total_cost * 2 / 5  # 2/5 of the total cost
    remaining_cost = total_cost - emp_salary
    delivery_cost = remaining_cost * 1 / 4  # 1/4 of the remaining cost
    remaining_cost -= delivery_cost
    order_cost = remaining_cost
    result = order_cost
    return result

print(solution())