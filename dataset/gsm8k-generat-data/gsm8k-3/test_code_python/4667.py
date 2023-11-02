def solution():
    """A 1165 cm long rope is cut into 154 pieces. 150 of the pieces are equally sized and the remaining pieces are 100mm each. Find the length of each of the equal pieces in millimeters."""
    # Convert rope length to millimeters
    rope_length = 1165 * 10

    # Calculate total length of the remaining pieces
    remaining_length = 100 * 4

    # Calculate total length of the 150 equally sized pieces
    equal_pieces_length = rope_length - remaining_length

    # Calculate length of each equal piece
    length_per_piece = equal_pieces_length / 150

    # Convert length per piece from millimeters to centimeters and round to 2 decimal places
    length_per_piece = round(length_per_piece / 10, 2)

    # Display length per piece
    result = length_per_piece
    return result

print(solution())