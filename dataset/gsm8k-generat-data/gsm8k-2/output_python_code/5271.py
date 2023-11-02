def solution():
    """Sweet Hope hosts a casino with 3 roulette tables labeled A, B, and C. At 6:00 pm, Table B had twice as much money on it as table C, which had $20 more than table A. If there was $40 on table A, how much money was there on all the tables?"""
    table_a_money = 40
    table_c_money = table_a_money + 20
    table_b_money = 2 * table_c_money
    total_money = table_a_money + table_b_money + table_c_money
    result = total_money
    return result

print(solution())