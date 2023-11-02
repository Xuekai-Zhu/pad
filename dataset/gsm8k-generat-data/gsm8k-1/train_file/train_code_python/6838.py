def solution():
    """Rachel earned $200 babysitting. She spent 1/4 of the money on lunch. She spent 1/2 of the money on a DVD. How much did Rachel have left?"""
    total_money = 200
    lunch_cost = total_money / 4
    dvd_cost = total_money / 2
    money_left = total_money - (lunch_cost + dvd_cost)
    result = money_left
    return result

print(solution())