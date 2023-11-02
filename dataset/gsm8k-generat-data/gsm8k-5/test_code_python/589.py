def solution():
    rectangular_tables = 7  # The library has 7 rectangular tables
    rectangular_table_capacity = 10  # A rectangular table seats 10 pupils
    total_capacity_rectangular_tables = rectangular_tables * rectangular_table_capacity  # Calculate the total capacity of the rectangular tables

    # Calculate the number of square tables needed
    square_table_capacity = 4  # A square table seats 4 pupils
    square_tables_needed = (90 - total_capacity_rectangular_tables) / square_table_capacity

    result = square_tables_needed
    return result

print(solution())