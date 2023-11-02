def solution():
    tables_this_month = 10  # The carpenter made 10 tables this month
    tables_last_month = tables_this_month - 3  # The carpenter made 3 fewer tables last month

    # Calculate the total number of tables the carpenter made
    total_tables = tables_this_month + tables_last_month
    result = total_tables
    return result

print(solution())