def solution():
    # Calculate the amount of money on table A, B, and C
    money_A = 40
    money_C = money_A + 20
    money_B = 2 * money_C

    # Calculate the total money on all tables
    total_money = money_A + money_B + money_C
    result = total_money
    return result

print(solution())