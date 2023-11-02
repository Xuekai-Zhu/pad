def solution():
    """Michael has $42. Michael gives away half the money to his brother. His brother then buys 3 dollars worth of candy. If his brother has $35 left, how much money, in dollars, did his brother have at first?"""
    michael_money = 42
    brother_money = michael_money / 2 - 3 + 35
    result = brother_money * 2

    return result

print(solution())