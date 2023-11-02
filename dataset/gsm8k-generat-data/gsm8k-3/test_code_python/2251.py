def solution():
    """Tom has a job mowing lawns around his neighborhood. Each month he spends $17 on gas and mows 3 lawns, charging $12 per lawn mowed. Last month he also made extra money pulling weeds for $10. How much profit did Tom earn last month?"""

    # Define the cost of gas and the price per lawn mowed
    GAS_COST = 17
    LAWN_PRICE = 12

    # Calculate Tom's revenue from mowing lawns
    lawn_revenue = 3 * LAWN_PRICE

    # Calculate Tom's total profit, including the money made pulling weeds
    total_profit = lawn_revenue - GAS_COST + 10

    # Display Tom's profit
    result = total_profit
    return result

print(solution())