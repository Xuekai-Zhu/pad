def solution():
    """A 1165 cm long rope is cut into 154 pieces. 150 of the pieces are equally sized and the remaining pieces are 100mm each. Find the length of each of the equal pieces in millimeters."""
    total_length = 1165
    num_equal_pieces = 150
    remaining_length = total_length - (num_equal_pieces * 100)
    length_per_equal_piece = remaining_length / num_equal_pieces
    result = length_per_equal_piece * 10  # convert to millimeters
    return result

print(solution())