def solution():
    """Ben will receive a bonus of $1496. He chooses to allocate this amount as follows: 1/22 for the kitchen, 1/4 for holidays and 1/8 for Christmas gifts for his 3 children. How much money will he still have left after these expenses?"""
    bonus = 1496
    kitchen_share = bonus / 22
    holiday_share = bonus / 4
    children_gift_share = bonus / 8 / 3
    total_expense = kitchen_share + holiday_share + children_gift_share
    leftover = bonus - total_expense
    result = leftover
    return result

print(solution())