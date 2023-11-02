def solution():
    rectangular_tables = 7
    remaining_tables = rectangular_tables - 7
    square_tables = remaining_tables
    pupils_seated = 10 * rectangular_tables + 4 * square_tables
    result = square_tables
    
    return result

print(solution())