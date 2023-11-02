def solution():
    """To run his grocery store, Mr. Haj needs $4000 a day. This money is used to pay for orders done, delivery costs and employees' salaries. If he spends 2/5 of the total operation costs on employees' salary and 1/4 of the remaining amount on delivery costs, how much money does he pay for the orders done?"""
    # Define the total operation cost and the percentage allocated to employee salaries and delivery costs
    total_cost = 4000
    salary_percentage = 0.4
    delivery_percentage = 0.25

    # Calculate the amount allocated to employee salaries
    salary_cost = total_cost * salary_percentage

    # Calculate the remaining amount after paying for employee salaries
    remaining_cost = total_cost - salary_cost

    # Calculate the amount allocated to delivery costs
    delivery_cost = remaining_cost * delivery_percentage

    # Calculate the amount allocated to orders done
    order_cost = remaining_cost - delivery_cost

    # return the result
    result = order_cost
    return result

print(solution())