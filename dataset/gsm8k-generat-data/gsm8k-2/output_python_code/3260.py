def solution():
    """Benny is baking pies for a bake sale. He plans to make ten pumpkin pies, which cost $3 each to make, and twelve cherry pies, which cost $5 each to make. If he wants to make a profit of $20 selling all the pies, how much does he have to charge for each pie if both kinds sell at the same price?"""
    pumpkin_pie_cost = 3
    cherry_pie_cost = 5
    total_pumpkin_pie_cost = 10 * pumpkin_pie_cost
    total_cherry_pie_cost = 12 * cherry_pie_cost
    total_cost = total_pumpkin_pie_cost + total_cherry_pie_cost
    total_revenue = total_cost + 20
    total_pies = 10 + 12
    price_per_pie = total_revenue / total_pies
    result = price_per_pie
    return result

print(solution())