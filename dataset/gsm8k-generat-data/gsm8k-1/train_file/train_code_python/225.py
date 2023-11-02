def solution():
    """There are 32 tables in a hall. Half the tables have 2 chairs each, 5 have 3 chairs each and the rest have 4 chairs each. How many chairs in total are in the hall?"""
    total_tables = 32
    half_tables = int(total_tables / 2)
    tables_with_two_chairs = half_tables
    tables_with_three_chairs = 5
    tables_with_four_chairs = total_tables - tables_with_two_chairs - tables_with_three_chairs
    
    total_chairs = (tables_with_two_chairs * 2) + (tables_with_three_chairs * 3) + (tables_with_four_chairs * 4)
    
    result = total_chairs
    return result

print(solution())