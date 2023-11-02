def solution():
    """Raymond had $21. Then he saved $11 from his allowance and spent $5 on a comic book and $19 on a puzzle. How much money does Raymond have left?"""
    starting_money = 21
    allowance_saved = 11
    money_spent = 5 + 19
    remaining_money = starting_money + allowance_saved - money_spent
    result = remaining_money
    return result

print(solution())