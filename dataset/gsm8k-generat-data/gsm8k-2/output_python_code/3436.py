def solution():
    """John receives $100 from his uncle and gives his sister Jenna 1/4 of that money. He goes and buys groceries worth $40. How much money does John have remaining?"""
    starting_money = 100
    sister_money = starting_money / 4
    john_money = starting_money - sister_money - 40
    result = john_money
    return result

print(solution())