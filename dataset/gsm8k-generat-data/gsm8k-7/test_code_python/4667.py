def solution():
    total_length = 1165
    num_pieces = 154
    num_equal_pieces = 150
    length_of_remaining_pieces = 100

    # Calculate the total length of the remaining pieces
    total_length_remaining_pieces = (num_pieces - num_equal_pieces) * length_of_remaining_pieces

    # Calculate the total length of the equal pieces
    total_length_equal_pieces = total_length - total_length_remaining_pieces

    # Calculate the length of one equal piece in millimeters
    length_of_one_equal_piece = total_length_equal_pieces / num_equal_pieces * 10

    result = length_of_one_equal_piece
    return result

print(solution())