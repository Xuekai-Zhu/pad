def solution():
    rope_length = 1165  # The length of the rope is 1165 cm
    num_pieces = 154  # The rope is cut into 154 pieces
    num_equal_pieces = 150  # 150 of the pieces are equally sized
    length_of_remaining_pieces = 100  # The remaining pieces are each 100mm long

    # Calculate the total length of the remaining pieces in centimeters
    length_of_remaining_pieces_cm = length_of_remaining_pieces * (num_pieces - num_equal_pieces) / 10

    # Calculate the total length of the equal pieces in centimeters
    length_of_equal_pieces_cm = rope_length - length_of_remaining_pieces_cm

    # Calculate the length of each equal piece in millimeters
    length_of_equal_pieces_mm = length_of_equal_pieces_cm / num_equal_pieces * 10
    result = length_of_equal_pieces_mm
    return result

print(solution())