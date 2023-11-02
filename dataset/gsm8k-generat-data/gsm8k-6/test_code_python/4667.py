def solution():
    # Convert the length of the rope to millimeters
    rope_length_mm = 1165 * 10

    # Calculate the length of the 100mm pieces in millimeters
    short_pieces_length_mm = 100

    # Calculate the total length of the short pieces in millimeters
    total_short_pieces_length_mm = short_pieces_length_mm * (154 - 150)

    # Calculate the length of the equal pieces in millimeters
    equal_pieces_length_mm = (rope_length_mm - total_short_pieces_length_mm) / 150

    result = equal_pieces_length_mm
    return result

print(solution())