def solution():
    half_money = 43
    money_before_giving = half_money * 2
    jerome_money = money_before_giving
    meg_money = 8
    bianca_money = 3 * meg_money

    # Calculate how much money Jerome has left
    jerome_money_left = jerome_money - meg_money - bianca_money
    result = jerome_money_left
    return result

print(solution())