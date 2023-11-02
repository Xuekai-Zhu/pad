def solution():
    total_length = 51 * 100  # Convert meters to centimeters
    length_per_piece = 15
    num_pieces = 100

    # Calculate the total length of ribbon used for 100 pieces
    total_length_used = length_per_piece * num_pieces

    # Calculate the remaining length of ribbon
    remaining_length = total_length - total_length_used
    result = remaining_length
    return result

print(solution())