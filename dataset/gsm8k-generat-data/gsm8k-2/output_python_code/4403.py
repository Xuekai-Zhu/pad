def solution():
    """John sells 20 woodburning for $15 each. The wood cost $100. How much does he make in profit?"""
    num_woodburning = 20
    price_per_woodburning = 15
    total_sales = num_woodburning * price_per_woodburning
    cost_of_wood = 100
    total_costs = cost_of_wood
    total_profit = total_sales - total_costs
    result = total_profit
    return result

print(solution())