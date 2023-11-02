def solution():
    """Sweet Hope hosts a casino with 3 roulette tables labeled A, B, and C. At 6:00 pm, Table B had twice as much money on it as table C, which had $20 more than table A. If there was $40 on table A, how much money was there on all the tables?"""
    # Define the initial amount of money on table A
    table_a = 40

    # Calculate the amount of money on table C
    table_c = table_a + 20

    # Calculate the amount of money on table B
    table_b = table_c * 2

    # Calculate the total amount of money on all tables
    total_money = table_a + table_b + table_c

    result = total_money
    return result

print(solution())