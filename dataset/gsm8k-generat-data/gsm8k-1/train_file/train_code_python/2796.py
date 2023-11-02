def solution():
    """To run his grocery store, Mr. Haj needs $4000 a day. This money is used to pay for orders done, delivery costs and employees' salaries.
    If he spends 2/5 of the total operation costs on employees' salary and 1/4 of the remaining amount on delivery costs,
    how much money does he pay for the orders done?"""
    total_cost = 4000
    employee_salary = total_cost * (2/5)
    remaining_cost = total_cost - employee_salary
    delivery_cost = remaining_cost * (1/4)
    order_cost = remaining_cost - delivery_cost
    result = order_cost
    return result

print(solution())