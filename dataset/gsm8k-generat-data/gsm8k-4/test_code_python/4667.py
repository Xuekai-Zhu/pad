def solution():
    """A 1165 cm long rope is cut into 154 pieces. 150 of the pieces are equally sized and the remaining pieces are 100mm each. Find the length of each of the equal pieces in millimeters."""
    # Convert the length of the rope from cm to mm
    rope_length_mm = 1165 * 10

    # Calculate the total length of the remaining pieces in mm
    remaining_length_mm = 100 * (154 - 150)

    # Calculate the total length of the equal pieces in mm
    equal_length_mm = rope_length_mm - remaining_length_mm

    # Calculate the length of each equal piece in mm
    equal_piece_length_mm = equal_length_mm / 150

    # Return the result
    result = equal_piece_length_mm
    return result

print(solution())