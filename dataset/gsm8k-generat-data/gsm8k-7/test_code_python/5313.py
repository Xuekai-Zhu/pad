def solution():
    total_cake_pieces = 240
    eaten_cake_pieces = total_cake_pieces * 0.6
    remaining_cake_pieces = total_cake_pieces - eaten_cake_pieces
    sisters = 3

    # Calculate the number of cake pieces each sister received
    pieces_per_sister = remaining_cake_pieces / sisters
    result = pieces_per_sister
    return result

print(solution())