def solution():
    # Calculate number of tables with 2 chairs each
    tables_with_2 = 0.5 * 32
    chairs_from_tables_with_2 = tables_with_2 * 2

    # Calculate number of tables with 3 chairs each
    chairs_from_tables_with_3 = 5 * 3

    # Calculate number of tables with 4 chairs each
    tables_with_4 = 32 - tables_with_2 - 5
    chairs_from_tables_with_4 = tables_with_4 * 4

    # Calculate total number of chairs
    total_chairs = chairs_from_tables_with_2 + chairs_from_tables_with_3 + chairs_from_tables_with_4
    result = total_chairs
    return result

print(solution())