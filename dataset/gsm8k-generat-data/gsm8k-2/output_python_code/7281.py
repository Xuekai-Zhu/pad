def solution():
    """Oliver has $40 and 200 quarters. If he gives his sister $5 and 120 quarters, how much money in total is he left with?"""
    start_money = 40 + (200 * 0.25)
    money_given = 5 + (120 * 0.25)
    remaining_money = start_money - money_given
    result = remaining_money
    return result

print(solution())