def solution():
    """Twice the money Jericho has is 60. He owes Annika $14 and also owes half as much to Manny. After paying off all his debts, how much money will Jericho be left with?"""
    twice_money = 60
    money = twice_money / 2
    annika_debt = 14
    manny_debt = annika_debt / 2
    total_debt = annika_debt + manny_debt
    remaining_money = money - total_debt
    result = remaining_money
    return result

print(solution())