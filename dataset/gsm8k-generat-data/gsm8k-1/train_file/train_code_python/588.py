def solution():
    """A library has 7 rectangular tables and the remaining tables will be square tables. A rectangular table seats 10 pupils while a square table seats 4 pupils. How many square tables are needed so that 90 pupils can read at the same time?"""
    rectangular_tables = 7
    rectangular_seating = 10
    total_seating = rectangular_tables * rectangular_seating
    remaining_seating_needed = 90 - total_seating
    square_seating = 4
    square_tables_needed = remaining_seating_needed / square_seating
    result = square_tables_needed
    return result

print(solution())