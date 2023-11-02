def solution():
    # Define the number of tables made this month
    tables_this_month = 10

    # Calculate the number of tables made last month
    tables_last_month = tables_this_month - 3

    # Calculate the total number of tables
    total_tables = tables_this_month + tables_last_month
    result = total_tables
    return result

print(solution())