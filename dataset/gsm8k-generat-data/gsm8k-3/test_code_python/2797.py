def solution():
    """To run his grocery store, Mr. Haj needs $4000 a day. This money is used to pay for orders done, delivery costs and employees' salaries. If he spends 2/5 of the total operation costs on employees' salary and 1/4 of the remaining amount on delivery costs, how much money does he pay for the orders done?"""
    # Define the total operation costs
    total_cost = 4000

    # Calculate the amount spent on employees' salaries
    salary_cost = total_cost * (2/5)

    # Calculate the amount remaining after paying for employees' salaries
    remaining_cost = total_cost - salary_cost

    # Calculate the amount spent on delivery costs
    delivery_cost = remaining_cost * (1/4)

    # Calculate the amount spent on orders done
    order_cost = remaining_cost - delivery_cost

    # Display the amount spent on orders done
    result = order_cost
    return result

print(solution())