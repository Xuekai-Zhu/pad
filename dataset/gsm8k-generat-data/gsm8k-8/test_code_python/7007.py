def solution():
    total_pieces = 100
    pieces_per_level = 7
    remaining_pieces = 23

    # Calculate the total number of pieces used in the tower
    used_pieces = total_pieces - remaining_pieces

    # Calculate the number of complete levels in the tower
    complete_levels = used_pieces // pieces_per_level

    result = complete_levels
    return result

print(solution())