def solution():
    """Peter is buying a set of glasses. They cost $3 for small glasses and $5 for large ones. He has $50. If he buys 8 small ones and leaves with $1 in change, how many large ones did he buy?"""
    small_price = 3
    large_price = 5
    small_count = 8
    total_spent = (small_price * small_count) + 1
    money_left = 50 - total_spent
    large_count = money_left // large_price
    result = large_count
    return result

print(solution())