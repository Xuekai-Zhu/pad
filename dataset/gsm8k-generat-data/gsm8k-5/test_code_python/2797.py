def solution():
    total_cost = 4000  # Mr. Haj needs $4000 a day for the grocery store
    employee_salary = (2/5) * total_cost  # 2/5 of the total cost is spent on employee salaries
    remaining_cost = total_cost - employee_salary  # The remaining cost after paying employee salaries
    delivery_cost = (1/4) * remaining_cost  # 1/4 of the remaining cost is spent on delivery costs

    # The rest of the cost is spent on orders done
    order_cost = remaining_cost - delivery_cost
    result = order_cost
    return result

print(solution())