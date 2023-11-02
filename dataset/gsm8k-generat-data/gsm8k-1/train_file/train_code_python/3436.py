def solution():
    """John receives $100 from his uncle and gives his sister Jenna 1/4 of that money. He goes and buys groceries worth $40. How much money does John have remaining?"""
    initial_money = 100
    money_given_to_sister = initial_money / 4
    money_remaining = initial_money - money_given_to_sister - 40
    result = money_remaining
    return result

print(solution())