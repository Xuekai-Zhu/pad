def solution():
    """Peter is buying a set of glasses. They cost $3 for small glasses and $5 for large ones. He has $50. If he buys 8 small ones and leaves with $1 in change, how many large ones did he buy?"""
    small_price = 3
    large_price = 5
    small_count = 8
    budget = 50
    change = 1
    
    total_small_price = small_price * small_count
    remaining_budget = budget - total_small_price - change
    large_count = remaining_budget // large_price
    
    result = large_count
    return result

print(solution())