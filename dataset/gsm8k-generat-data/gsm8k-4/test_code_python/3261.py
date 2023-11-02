def solution():
    """Benny is baking pies for a bake sale. He plans to make ten pumpkin pies, which cost $3 each to make, and twelve cherry pies, which cost $5 each to make. If he wants to make a profit of $20 selling all the pies, how much does he have to charge for each pie if both kinds sell at the same price?"""
    # Define the number of pumpkin and cherry pies
    pumpkin_pies = 10
    cherry_pies = 12

    # Define the cost of making each pumpkin and cherry pie
    pumpkin_cost = 3
    cherry_cost = 5

    # Calculate the total cost of making all the pies
    total_cost = (pumpkin_pies * pumpkin_cost) + (cherry_pies * cherry_cost)

    # Calculate the total revenue needed to make a profit of $20
    total_revenue_needed = total_cost + 20

    # Calculate the price to charge for each pie
    price_per_pie = total_revenue_needed / (pumpkin_pies + cherry_pies)

    # return the result
    result = price_per_pie
    return result

print(solution())