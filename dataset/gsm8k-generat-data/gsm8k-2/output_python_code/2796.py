def solution():
    """To run his grocery store, Mr. Haj needs $4000 a day. This money is used to pay for orders done, delivery costs and employees' salaries. If he spends 2/5 of the total operation costs on employees' salary and 1/4 of the remaining amount on delivery costs, how much money does he pay for the orders done?"""
    total_operation_cost = 4000
    emp_salaries = total_operation_cost * 2/5
    remaining_cost = total_operation_cost - emp_salaries
    delivery_cost = remaining_cost * 1/4
    total_other_expenses = emp_salaries + delivery_cost
    orders_cost = total_operation_cost - total_other_expenses
    result = orders_cost
    return result

print(solution())