def solution():
    """Benny is baking pies for a bake sale. He plans to make ten pumpkin pies, which cost $3 each to make,
     and twelve cherry pies, which cost $5 each to make. If he wants to make a profit of $20 selling all the pies,
     how much does he have to charge for each pie if both kinds sell at the same price?"""
    # Define the cost and revenue per pie for both types of pies
    PUMPKIN_COST = 3
    CHERRY_COST = 5
    TOTAL_PIES = 22
    PROFIT = 20

    # Calculate the total cost to make all the pies
    total_cost = (10 * PUMPKIN_COST) + (12 * CHERRY_COST)

    # Calculate the revenue needed to make a profit of $20
    revenue_needed = total_cost + PROFIT

    # Calculate the price per pie needed to reach the revenue goal
    price_per_pie = revenue_needed / TOTAL_PIES

    # Display the price per pie
    result = price_per_pie
    return result

print(solution())