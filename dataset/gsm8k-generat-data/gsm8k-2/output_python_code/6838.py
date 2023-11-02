def solution():
    """Rachel earned $200 babysitting. She spent 1/4 of the money on lunch. She spent 1/2 of the money on a DVD. How much did Rachel have left?"""
    total_money = 200
    lunch_money = total_money / 4
    dvd_money = total_money / 2
    remaining_money = total_money - lunch_money - dvd_money
    result = remaining_money
    return result

print(solution())