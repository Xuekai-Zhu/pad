def solution():
    money_on_table_a = 40  # Table A had $40 on it
    money_on_table_c = money_on_table_a + 20  # Table C had $20 more than Table A
    money_on_table_b = 2 * money_on_table_c  # Table B had twice as much as Table C

    # Calculate the total money on all tables
    total_money = money_on_table_a + money_on_table_b + money_on_table_c
    result = total_money
    return result

print(solution())