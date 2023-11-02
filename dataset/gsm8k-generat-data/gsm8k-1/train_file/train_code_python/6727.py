def solution():
    """Michael has $42. His brother has $17. Michael gives away half the money to his brother. His brother then buys 3 dollars worth of candy. How much money, in dollars, did his brother have in the end?"""
    michael_money = 42
    brother_money = 17
    michael_gives = michael_money / 2
    brother_money += michael_gives
    brother_money -= 3
    result = brother_money
    return result

print(solution())