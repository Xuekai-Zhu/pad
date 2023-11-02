def solution():
    # Convert the total length of the rope to millimeters
    rope_length_mm = 1165 * 10

    # Calculate the total length of the 100mm pieces
    remaining_length = 100 * (154 - 150)

    # Subtract the length of the remaining pieces from the total length to get the length of the equal pieces
    equal_length = (rope_length_mm - remaining_length) / 150

    result = equal_length
    return result

print(solution())