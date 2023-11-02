def solution():
    # Calculate the number of tables with 2 chairs
    tables_with_2_chairs = 32 / 2  # half the tables have 2 chairs each

    # Calculate the number of tables with 3 chairs
    tables_with_3_chairs = 5

    # Calculate the number of tables with 4 chairs
    tables_with_4_chairs = 32 - tables_with_2_chairs - tables_with_3_chairs

    # Calculate the total number of chairs in the hall
    total_chairs = tables_with_2_chairs * 2 + tables_with_3_chairs * 3 + tables_with_4_chairs * 4
    result = total_chairs
    return result

print(solution())