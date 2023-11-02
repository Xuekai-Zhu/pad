def solution():
    """Tom has a job mowing lawns around his neighborhood. Each month he spends $17 on gas and mows 3 lawns, charging $12 per lawn mowed. Last month he also made extra money pulling weeds for $10. How much profit did Tom earn last month?"""
    # Define the gas cost and lawn mowing revenue
    GAS_COST = 17
    LAWN_MOWING_REVENUE = 12 * 3

    # Calculate the total revenue
    total_revenue = LAWN_MOWING_REVENUE + 10

    # Calculate the total cost
    total_cost = GAS_COST

    # Calculate the profit
    profit = total_revenue - total_cost

    result = profit
    return result

print(solution())