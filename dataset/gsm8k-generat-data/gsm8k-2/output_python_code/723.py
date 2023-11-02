def solution():
    """Jenny had $24 left after spending 3/7 of her money. How much is half of her original amount of money?"""
    money_left = 24
    money_spent_fraction = 3/7
    remaining_fraction = 1 - money_spent_fraction
    total_money = money_left / remaining_fraction
    half_money = total_money / 2
    result = half_money
    return result

print(solution())