def solution():
    """Ben will receive a bonus of $1496. He chooses to allocate this amount as follows: 1/22 for the kitchen, 1/4 for holidays and 1/8 for Christmas gifts for his 3 children. How much money will he still have left after these expenses?"""
    total_bonus = 1496
    kitchen_share = total_bonus / 22
    holiday_share = total_bonus / 4
    children_share = total_bonus / 8 / 3
    total_expenses = kitchen_share + holiday_share + children_share
    remaining_money = total_bonus - total_expenses
    result = remaining_money
    return result

print(solution())