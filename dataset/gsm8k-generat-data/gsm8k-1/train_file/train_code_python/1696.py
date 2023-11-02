def solution():
    """There were 21 dollars in the cookie jar. Doris spent $6 from the cookie jar. Martha spent half as much as Doris. How much money, in dollars, was left in the cookie jar?"""
    total_money = 21
    doris_spent = 6
    martha_spent = doris_spent / 2
    money_left = total_money - (doris_spent + martha_spent)
    result = money_left
    return result

print(solution())