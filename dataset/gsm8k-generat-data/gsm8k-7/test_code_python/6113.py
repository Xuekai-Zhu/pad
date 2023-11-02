def solution():
    num_tables_4seats = 6
    seats_per_table_4seats = 4

    num_tables_6seats = 12
    seats_per_table_6seats = 6

    # Calculate the total number of seats needed for tables with 4 seats
    total_seats_4seats = num_tables_4seats * seats_per_table_4seats

    # Calculate the total number of seats needed for tables with 6 seats
    total_seats_6seats = num_tables_6seats * seats_per_table_6seats

    # Calculate the total number of chairs needed
    total_chairs = total_seats_4seats + total_seats_6seats
    result = total_chairs
    return result

print(solution())