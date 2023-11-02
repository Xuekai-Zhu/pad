def solution():
    """John sells 20 woodburning for $15 each. The wood cost $100. How much does he make in profit?"""
    num_woodburning = 20
    price_per_woodburning = 15
    total_sales = num_woodburning * price_per_woodburning
    cost_of_wood = 100
    total_cost = cost_of_wood
    profit = total_sales - total_cost
    result = profit
    
    return result

print(solution())