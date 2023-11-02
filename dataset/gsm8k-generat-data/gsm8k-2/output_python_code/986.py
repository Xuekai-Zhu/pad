def solution():
    """If Lucy would give Linda $5, Lucy would have the same amount of money as Linda. If Lucy originally had $20, how much money did Linda have at the beginning?"""
    lucy_money = 20
    linda_money = (lucy_money - 5) * 2
    result = linda_money
    return result

print(solution())