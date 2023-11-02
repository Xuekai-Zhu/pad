def solution():
    
    rectangular_tables = 7
    rectangular_seating = 10
    total_seating = rectangular_tables * rectangular_seating
    remaining_seating_needed = 90 - total_seating
    square_seating = 4
    square_tables_needed = remaining_seating_needed / square_seating
    result = square_tables_needed
    return result

print(solution())