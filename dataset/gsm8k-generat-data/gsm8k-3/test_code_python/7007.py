def solution():
    """Jade is building a lego tower. She has 100 pieces. Each level has to be 7 pieces wide. If she has 23 pieces left at the end, how many levels is her tower?"""
    # Define the number of lego pieces and the width of each level
    total_pieces = 100
    level_width = 7

    # Calculate the number of full levels and the remaining pieces
    full_levels = total_pieces // level_width
    remaining_pieces = total_pieces % level_width

    # Subtract the remaining pieces from the total to get the number of pieces used for full levels
    pieces_used = total_pieces - remaining_pieces

    # Calculate the number of levels from the pieces used and the level width
    num_levels = pieces_used // level_width

    # Display the number of levels
    result = num_levels
    return result

print(solution())