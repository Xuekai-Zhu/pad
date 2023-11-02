def solution():
    total_pieces = 1000  # total number of pieces in the puzzle
    first_day_pieces = 0.1 * total_pieces  # number of pieces Luke put together on the first day
    remaining_pieces = total_pieces - first_day_pieces  # number of pieces remaining after the first day
    second_day_pieces = 0.2 * remaining_pieces  # number of pieces Luke put together on the second day
    remaining_pieces = remaining_pieces - second_day_pieces  # number of pieces remaining after the second day
    third_day_pieces = 0.3 * remaining_pieces  # number of pieces Luke put together on the third day
    pieces_left = remaining_pieces - third_day_pieces  # number of pieces left to complete after the third day
    result = pieces_left
    return result

print(solution())