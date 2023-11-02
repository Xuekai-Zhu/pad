def solution():
    total_length = 72  # Vincent has a total of 72 inches of rope
    num_pieces = 12  # Vincent wants to cut the rope into 12 pieces
    piece_length = total_length / num_pieces  # Each piece will be of equal length

    # After tying three pieces together, the resulting length will be shorter by 1 inch
    shortened_length = piece_length - 1 

    # Calculate the total length after tying three pieces together
    total_shortened_length = shortened_length * 4

    result = total_shortened_length
    return result

print(solution())