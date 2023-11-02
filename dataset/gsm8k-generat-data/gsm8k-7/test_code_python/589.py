def solution():
    num_rectangular_tables = 7
    rectangular_table_capacity = 10
    square_table_capacity = 4
    num_pupils = 90

    # Calculate the total capacity of rectangular tables
    rectangular_table_total_capacity = num_rectangular_tables * rectangular_table_capacity

    # Calculate the number of pupils that need to sit at square tables
    num_pupils_at_square_tables = num_pupils - rectangular_table_total_capacity

    # Calculate the number of square tables needed
    num_square_tables = num_pupils_at_square_tables / square_table_capacity

    # Round up to the nearest integer
    num_square_tables = int(num_square_tables + 0.5)

    result = num_square_tables
    return result

print(solution())