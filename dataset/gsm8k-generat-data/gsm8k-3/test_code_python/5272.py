def solution():
    """Sweet Hope hosts a casino with 3 roulette tables labeled A, B, and C. At 6:00 pm, Table B had twice as much money on it as table C, which had $20 more than table A. If there was $40 on table A, how much money was there on all the tables?"""
    # Define the amount of money on Table A
    A_money = 40

    # Calculate the amount of money on Table C
    C_money = A_money + 20

    # Calculate the amount of money on Table B
    B_money = 2*C_money

    # Calculate the total amount of money on all tables
    total_money = A_money + B_money + C_money

    # Display the total amount of money
    result = total_money
    return result

print(solution())