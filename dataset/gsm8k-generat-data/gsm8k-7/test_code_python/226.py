def solution():
    num_tables = 32

    # Calculate the number of tables with 2 chairs and the total number of chairs in those tables
    num_tables_2_chairs = num_tables / 2
    total_chairs_2_chairs = num_tables_2_chairs * 2

    # Calculate the number of tables with 3 chairs and the total number of chairs in those tables
    num_tables_3_chairs = 5
    total_chairs_3_chairs = num_tables_3_chairs * 3

    # Calculate the number of tables with 4 chairs and the total number of chairs in those tables
    num_tables_4_chairs = num_tables - num_tables_2_chairs - num_tables_3_chairs
    total_chairs_4_chairs = num_tables_4_chairs * 4

    # Calculate the total number of chairs in the hall
    total_chairs = total_chairs_2_chairs + total_chairs_3_chairs + total_chairs_4_chairs
    result = total_chairs
    return result

print(solution())