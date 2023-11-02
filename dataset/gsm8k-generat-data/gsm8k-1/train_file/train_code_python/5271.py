def solution():
    """Sweet Hope hosts a casino with 3 roulette tables labeled A, B, and C. At 6:00 pm, Table B had twice as much money on it as table C, which had $20 more than table A. If there was $40 on table A, how much money was there on all the tables?"""
    money_on_a = 40
    money_on_c = money_on_a + 20
    money_on_b = 2*money_on_c
    total_money = money_on_a + money_on_b + money_on_c
    result = total_money
    return result

print(solution())