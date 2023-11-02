def solution():
    total_cake_pieces = 240  # The cake had 240 pieces
    eaten_cake_pieces = 0.6 * total_cake_pieces  # 60% of the cake was eaten
    remaining_cake_pieces = total_cake_pieces - eaten_cake_pieces  # The number of pieces remaining
    pieces_per_sister = remaining_cake_pieces / 3  # The pieces divided equally among three sisters
    result = pieces_per_sister
    return result

print(solution())