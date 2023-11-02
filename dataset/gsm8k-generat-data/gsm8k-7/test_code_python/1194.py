def solution():
    total_length = 72  # inches
    num_pieces = 12

    # Calculate the length of each initial piece before tying them together
    initial_piece_length = total_length / num_pieces

    # Calculate the new length of each piece after tying three pieces together
    new_piece_length = initial_piece_length - 1

    # Calculate the length of all pieces combined (before and after tying)
    total_piece_length = (initial_piece_length * num_pieces) + (new_piece_length * 4)

    result = total_piece_length
    return result

print(solution())