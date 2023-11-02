def solution():
    # Define the initial amount on Table A
    table_a_money = 40

    # Calculate the amount on Table C
    table_c_money = table_a_money + 20

    # Calculate the amount on Table B
    table_b_money = 2 * table_c_money

    # Calculate the total amount on all tables
    total_money = table_a_money + table_b_money + table_c_money
    result = total_money
    return result

print(solution())