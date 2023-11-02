def solution():
    """Mark buys a Magic card for $100, which then triples in value. How much profit would he make selling it?"""
    initial_cost = 100
    final_value = initial_cost * 3
    profit = final_value - initial_cost
    result = profit
    return result

print(solution())