def solution():
    """Rodney has 35 dollars more than Ian. Ian has half as much money as Jessica has. If Jessica has 100 dollars, how much more money does Jessica have than Rodney?"""
    jessica_money = 100
    ian_money = jessica_money / 2
    rodney_money = ian_money + 35
    difference = jessica_money - rodney_money
    result = difference
    return result

print(solution())