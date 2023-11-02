def solution():
    # Calculate the length of each of the 12 equal pieces
    piece_length = 72 / 12

    # Calculate the length of each piece after tying three together
    new_piece_length = (piece_length * 3) - 1

    # Calculate the new length of all 12 pieces
    new_length = new_piece_length * 12

    result = new_length
    return result

print(solution())