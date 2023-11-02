def solution():
    total_pieces = 100  # Jade has 100 lego pieces
    pieces_per_level = 7  # Each level has to be 7 pieces wide

    # Calculate the maximum number of levels Jade can build with the given pieces
    max_levels = total_pieces // pieces_per_level

    # Calculate the number of remaining pieces after building the maximum number of levels
    remaining_pieces = total_pieces - (max_levels * pieces_per_level)

    # If there are remaining pieces, add another level
    if remaining_pieces >= 7:
        levels = max_levels + 1
    else:
        levels = max_levels

    result = levels
    return result

print(solution())