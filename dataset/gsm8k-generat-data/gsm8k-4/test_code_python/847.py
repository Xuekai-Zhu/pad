def solution():
    """While cultivating a small farm, a farmer spent $50 on corn seeds, $35 on fertilizers and pesticides, and $15 on labor. After a successful harvest, he was able to gather 10 bags of corn. How much should he sell each bag, if he wants to make a profit of 10%?"""
    # Define the total cost of producing 10 bags of corn
    total_cost = 50 + 35 + 15

    # Calculate the desired profit
    desired_profit = total_cost * 0.1

    # Calculate the total revenue needed to achieve the desired profit
    total_revenue = total_cost + desired_profit

    # Calculate the revenue needed per bag of corn
    revenue_per_bag = total_revenue / 10

    # Return the result
    result = round(revenue_per_bag, 2)
    return result

print(solution())