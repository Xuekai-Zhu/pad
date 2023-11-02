def solution():
    """Lucy lost one-third of her money. She then spent one-fourth of the remainder, and only left with $15. How much money did Lucy have at the beginning?"""
    remaining_money = 15
    spent_money = remaining_money / (1/4)
    money_after_loss = spent_money * (3/4)
    initial_money = money_after_loss * (4/3)
    result = initial_money
    return result

print(solution())