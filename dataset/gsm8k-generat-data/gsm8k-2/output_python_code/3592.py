def solution():
    """Kate wants to buy a special pen as a gift for her friend. The pen costs $30, and Kate only has money for a third of that amount. How much more money does she need to buy the pen?"""
    pen_price = 30
    kate_money = pen_price / 3
    remaining_money = pen_price - kate_money
    result = remaining_money
    return result

print(solution())