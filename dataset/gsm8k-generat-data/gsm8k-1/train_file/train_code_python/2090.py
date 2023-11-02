def solution():
    """A store has an 8% discount on all items. If Shara paid $184 for a pair of shoes, how much did Shara save?"""
    original_price = 184/(1-0.08)
    discount = original_price - 184
    result = discount
    return result

print(solution())