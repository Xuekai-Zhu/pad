def solution():
    """Kate wants to buy a special pen as a gift for her friend. The pen costs $30, and Kate only has money for a third of that amount. How much more money does she need to buy the pen?"""
    pen_cost = 30
    available_money = pen_cost / 3
    money_needed = pen_cost - available_money
    result = money_needed
    return result

print(solution())