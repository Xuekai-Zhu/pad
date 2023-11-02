def solution():
    """Derek has $40. He spends $14 on lunch for himself, $11 for lunch for his dad, and $5 on more lunch for himself.
    His brother Dave has $50 and only spends $7 on lunch for his mom. How much more money does Dave have left than Derek?"""
    derek_spent = 14 + 11 + 5
    derek_left = 40 - derek_spent
    dave_spent = 7
    dave_left = 50 - dave_spent
    difference = dave_left - derek_left
    result = difference
    return result

print(solution())