def solution():
    """There are 32 tables in a hall. Half the tables have 2 chairs each, 5 have 3 chairs each and the rest have 4 chairs each. How many chairs in total are in the hall?"""
    # Define the total number of tables
    total_tables = 32

    # Calculate the number of tables with 2 chairs
    tables_with_2_chairs = total_tables // 2

    # Calculate the number of tables with 3 chairs
    tables_with_3_chairs = 5

    # Calculate the number of tables with 4 chairs
    tables_with_4_chairs = total_tables - tables_with_2_chairs - tables_with_3_chairs

    # Calculate the total number of chairs
    total_chairs = (tables_with_2_chairs * 2) + (tables_with_3_chairs * 3) + (tables_with_4_chairs * 4)

    # return the result
    result = total_chairs
    return result

print(solution())