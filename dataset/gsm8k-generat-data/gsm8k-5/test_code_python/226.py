def solution():
    # Calculate the number of tables with 2 chairs each
    tables_with_2_chairs = 32 / 2
    total_chairs_from_2_chairs = tables_with_2_chairs * 2

    # Calculate the number of tables with 3 chairs each
    total_chairs_from_3_chairs = 5 * 3

    # Calculate the number of tables with 4 chairs each
    tables_with_4_chairs = 32 - tables_with_2_chairs - 5
    total_chairs_from_4_chairs = tables_with_4_chairs * 4

    # Total number of chairs in the hall
    total_chairs = total_chairs_from_2_chairs + total_chairs_from_3_chairs + total_chairs_from_4_chairs
    result = total_chairs
    return result

print(solution())