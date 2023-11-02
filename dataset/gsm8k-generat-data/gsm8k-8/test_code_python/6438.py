def solution():
    # Calculate the total number of legs used for chairs
    chair_legs = 6 * 4

    # Calculate the remaining legs for tables
    table_legs = 40 - chair_legs

    # Calculate the number of tables based on 4 legs per table
    tables = table_legs / 4
    result = tables
    return result

print(solution())