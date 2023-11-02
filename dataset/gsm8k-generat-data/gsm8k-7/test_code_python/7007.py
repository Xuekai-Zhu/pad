def solution():
    total_pieces = 100
    pieces_per_level = 7
    leftover_pieces = 23

    # Calculate the total number of levels Jade can make
    total_levels = (total_pieces - leftover_pieces) / pieces_per_level

    result = total_levels
    return result

print(solution())