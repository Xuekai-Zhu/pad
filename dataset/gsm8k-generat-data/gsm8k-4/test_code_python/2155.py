def solution():
    """Tilly needs to sell 100 bags at $10 per bag to make $300 in profit. How much did she buy each bag for?"""
    # Define the desired profit and the number of bags
    PROFIT = 300
    NUM_BAGS = 100

    # Calculate the total revenue from selling the bags
    total_revenue = NUM_BAGS * 10

    # Calculate the total cost of buying the bags
    total_cost = total_revenue - PROFIT

    # Calculate the cost per bag
    cost_per_bag = total_cost / NUM_BAGS

    # Return the result
    result = cost_per_bag
    return result

print(solution())