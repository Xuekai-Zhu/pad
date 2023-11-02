def solution():
    """While cultivating a small farm, a farmer spent $50 on corn seeds, $35 on fertilizers and pesticides, and $15 on labor. After a successful harvest, he was able to gather 10 bags of corn. How much should he sell each bag, if he wants to make a profit of 10%?"""
    # Define the cost of production
    cost = 50 + 35 + 15

    # Calculate the profit percentage
    profit_percent = 10/100

    # Calculate the profit
    profit = cost * profit_percent

    # Calculate the total price
    total_price = cost + profit

    # Calculate the price per bag of corn
    price_per_bag = total_price/10

    # Display the price per bag
    result = price_per_bag
    return result

print(solution())