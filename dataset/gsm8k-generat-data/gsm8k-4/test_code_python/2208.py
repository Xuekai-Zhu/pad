def solution():
    """Steve is building a bench for the playground and needs 6 lengths of wood that measure 4 feet and 2 lengths of wood that measure 2 feet. How many feet of wood does Steve need to buy?"""
    # Define the length of each piece of wood
    long_piece = 4
    short_piece = 2

    # Define the number of pieces of each size needed
    long_pieces_needed = 6
    short_pieces_needed = 2

    # Calculate the total length of wood needed
    total_length_needed = (long_piece * long_pieces_needed) + (short_piece * short_pieces_needed)

    result = total_length_needed
    return result

print(solution())