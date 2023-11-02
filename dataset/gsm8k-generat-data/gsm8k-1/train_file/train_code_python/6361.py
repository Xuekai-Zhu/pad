def solution():
    """Frank spent 1/5 of his money to buy groceries. He then spent 1/4 of the remaining money to buy a magazine. If he had $360 left in his wallet, how much money did he have at first?"""
    money_left = 360
    remaining_money_after_magazine = money_left * 4
    money_before_magazine = remaining_money_after_magazine * 5
    result = money_before_magazine
    return result

print(solution())