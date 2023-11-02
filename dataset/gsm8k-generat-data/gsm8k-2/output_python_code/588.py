def solution():
    """A library has 7 rectangular tables and the remaining tables will be square tables. A rectangular table seats 10 pupils while a square table seats 4 pupils. How many square tables are needed so that 90 pupils can read at the same time?"""
    total_seats = 7 * 10 + x * 4  # Let x be the number of square tables needed
    remaining_pupils = 90 - (7 * 10)  # Total number of pupils minus the number of pupils seated at rectangular tables
    square_tables_needed = remaining_pupils // 4  # Number of square tables needed to seat all remaining pupils
    if remaining_pupils % 4 != 0:
        square_tables_needed += 1  # If there are still remaining pupils not seated after adding up all the square tables, round up to the nearest whole number of square tables
    result = square_tables_needed
    return result

print(solution())