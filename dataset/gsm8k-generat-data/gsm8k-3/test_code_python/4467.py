def solution():
    """Julie is making caesar salad for a family picnic. At the market, she spends $8 on green lettuce and $6 on red lettuce. If each type of lettuce costs $2 per pound, how many total pounds of lettuce did she buy?"""
    # Define the cost of each type of lettuce and the total spent
    GREEN_LETTUCE_COST = 8
    RED_LETTUCE_COST = 6
    LETTUCE_COST_PER_POUND = 2
    total_spent = GREEN_LETTUCE_COST + RED_LETTUCE_COST

    # Calculate the total weight of lettuce purchased
    total_weight = total_spent / LETTUCE_COST_PER_POUND

    # Display the total weight of lettuce purchased
    result = total_weight
    return result

print(solution())