def solution():
    """Tilly needs to sell 100 bags at $10 per bag to make $300 in profit. How much did she buy each bag for?"""
    # Define the number of bags to be sold and the desired profit
    bags = 100
    profit = 300

    # Calculate the total revenue needed to make the desired profit
    revenue = (bags * 10) + profit

    # Calculate the cost of the bags
    cost_per_bag = revenue / bags

    # Display the cost per bag
    result = cost_per_bag
    return result

print(solution())