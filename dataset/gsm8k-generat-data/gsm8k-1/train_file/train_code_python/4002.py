def solution():
    """Joanna has $8. Compared to her money, her brother has thrice as much while her sister has only half as much. How much money do the three of them have altogether?"""
    joanna_money = 8
    brother_money = joanna_money * 3
    sister_money = joanna_money / 2
    total_money = joanna_money + brother_money + sister_money
    result = total_money
    return result

print(solution())