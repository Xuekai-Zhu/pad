def solution():
    """Kyle has $12 less than 3 times what Dave has. Kyle then spends a third of it going snowboarding. If Dave has $46, how much money does Kyle have?"""
    dave_money = 46
    kyle_money = 3 * dave_money - 12
    kyle_money_after_snowboarding = kyle_money - (kyle_money/3)
    result = kyle_money_after_snowboarding
    return result

print(solution())