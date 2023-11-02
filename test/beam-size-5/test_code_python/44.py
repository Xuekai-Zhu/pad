def solution():
    length_in_feet = 4  # in feet
    length_in_inches = 6  # in inches

    # Convert the length of the wire to inches
    length_in_inches = length_in_inches / 12

    # Calculate the total number of pieces
    total_pieces = length_in_inches / length_in_inches
    result = total_pieces
    return result

print(solution())