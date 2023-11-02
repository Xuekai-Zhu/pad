def solution():
    pieces_per_table = 12  # It takes 12 pieces of wood to make a table
    pieces_per_chair = 8  # It takes 8 pieces of wood to make a chair
    total_pieces = 672  # Gerald has 672 pieces of wood
    tables = 24  # Gerald wants to make 24 tables

    # Calculate the total pieces of wood used for the tables
    total_table_pieces = pieces_per_table * tables

    # Calculate the remaining pieces of wood available for chairs
    remaining_pieces = total_pieces - total_table_pieces

    # Calculate the number of chairs Gerald can make
    chairs = remaining_pieces // pieces_per_chair
    result = chairs
    return result

print(solution())