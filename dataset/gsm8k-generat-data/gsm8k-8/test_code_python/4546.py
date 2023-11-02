def solution():
    # Define the number of pieces of wood needed to make a table and a chair
    table_pieces = 12
    chair_pieces = 8

    # Calculate the total number of pieces of wood used for the tables
    total_table_pieces = 24 * table_pieces

    # Calculate the remaining pieces of wood after making the tables
    remaining_pieces = 672 - total_table_pieces

    # Calculate the number of chairs that can be made with the remaining pieces of wood
    num_chairs = remaining_pieces // chair_pieces
    result = num_chairs
    return result

print(solution())