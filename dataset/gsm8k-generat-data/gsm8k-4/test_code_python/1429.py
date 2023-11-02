def solution():
    """Ronald wants to make profits by re-selling some phones he bought a week ago. He bought 200 units for just $3000, and he wants to gain a third of the initial investment in profits when all units are sold. Including the profit margin, what will be the selling price for each phone?"""
    # Define the initial investment and desired profit
    initial_investment = 3000
    desired_profit_percentage = 33.33  # 1/3 of the initial investment

    # Calculate the desired profit
    desired_profit = initial_investment * (desired_profit_percentage / 100)

    # Calculate the total cost of the phones, including the desired profit
    total_cost = initial_investment + desired_profit

    # Calculate the cost per phone
    cost_per_phone = total_cost / 200

    # Add a profit margin of 10%
    selling_price = cost_per_phone * 1.1

    result = selling_price
    return result

print(solution())