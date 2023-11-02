def solution():
    """Benny is baking pies for a bake sale. He plans to make ten pumpkin pies, which cost $3 each to make, and twelve cherry pies, which cost $5 each to make. If he wants to make a profit of $20 selling all the pies, how much does he have to charge for each pie if both kinds sell at the same price?"""
    pumpkin_pies = 10
    pumpkin_cost = 3
    cherry_pies = 12
    cherry_cost = 5
    total_cost = (pumpkin_pies * pumpkin_cost) + (cherry_pies * cherry_cost)
    total_profit = 20
    total_pies = pumpkin_pies + cherry_pies
    price_per_pie = (total_cost + total_profit) / total_pies
    result = price_per_pie
    return result

print(solution())