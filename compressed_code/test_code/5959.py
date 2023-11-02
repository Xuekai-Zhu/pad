def solution():
    
    total_tables = 32
    half_tables = int(total_tables / 2)
    tables_with_two_chairs = half_tables
    tables_with_three_chairs = 5
    tables_with_four_chairs = total_tables - tables_with_two_chairs - tables_with_three_chairs
    
    total_chairs = (tables_with_two_chairs * 2) + (tables_with_three_chairs * 3) + (tables_with_four_chairs * 4)
    
    result = total_chairs
    return result

print(solution())