def solution():
    """Grover bought 3 boxes of face masks. He plans to sell them for $0.50 each. If each box has 20 face masks, and he bought the 3 boxes for $15, how much will be his total profit?"""
    # Define the cost of each box and the selling price of each mask
    COST_PER_BOX = 15 / 3
    SELLING_PRICE = 0.5

    # Calculate the total cost and total revenue
    total_cost = COST_PER_BOX * 3
    total_revenue = SELLING_PRICE * 60

    # Calculate the total profit
    total_profit = total_revenue - total_cost

    # Return the total profit
    result = total_profit
    return result

print(solution())