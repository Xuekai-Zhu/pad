def solution():
    """Derek has $40. He spends $14 on lunch for himself, $11 for lunch for his dad, and $5 on more lunch for himself. His brother Dave has $50 and only spends $7 on lunch for his mom. How much more money does Dave have left than Derek?"""
    derek_money = 40
    dave_money = 50
    derek_spending = 14 + 11 + 5
    dave_spending = 7
    derek_leftover = derek_money - derek_spending
    dave_leftover = dave_money - dave_spending
    difference = dave_leftover - derek_leftover
    result = difference
    return result

print(solution())