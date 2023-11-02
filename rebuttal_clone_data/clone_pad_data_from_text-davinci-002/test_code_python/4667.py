def solution():
    total_length = 1165
    total_pieces = 154
    big_pieces = 150
    small_pieces = total_pieces - big_pieces
    big_piece_length = (total_length - (small_pieces * 100)) / big_pieces
    result = big_piece_length
    return result

print(solution())