def solution():
    """There was some money in the cookie jar. Doris spent $6 from the cookie jar. Martha spent half as much as Doris. If there were $15 left in the cookie jar, how much money, in dollars, was there in the cookie jar at first?"""
    money_left = 15
    doris_spent = 6
    martha_spent = doris_spent / 2
    total_spent = doris_spent + martha_spent
    initial_money = money_left + total_spent
    result = initial_money
    return result

print(solution())