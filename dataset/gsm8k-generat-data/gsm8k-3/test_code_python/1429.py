def solution():
    """Ronald wants to make profits by re-selling some phones he bought a week ago. He bought 200 units for just $3000, and he wants to gain a third of the initial investment in profits when all units are sold. Including the profit margin, what will be the selling price for each phone?"""
    # Define the initial investment and the desired profit
    investment = 3000
    desired_profit = investment / 3

    # Calculate the total cost per phone, including the desired profit margin
    total_cost_per_phone = (investment + desired_profit) / 200

    # Display the selling price per phone
    result = total_cost_per_phone
    return result

print(solution())