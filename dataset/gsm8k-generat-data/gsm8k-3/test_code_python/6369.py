def solution():
    """A rope has a length of 200 meters. Stefan cuts the rope into four equal parts, gives his mother half of the cut pieces, and subdivides the remaining pieces into two more equal parts. What's the length of each piece?"""
    # Define the length of the rope
    rope_length = 200

    # Calculate the length of each cut piece
    cut_piece_length = rope_length / 4

    # Calculate the number of cut pieces Stefan gives to his mother
    mother_pieces = 2

    # Calculate the length of each cut piece Stefan keeps
    remaining_piece_length = cut_piece_length / 2

    # Calculate the total number of pieces Stefan has after giving half to his mother and subdividing the remaining pieces
    total_pieces = 2 + 2 * 2

    # Calculate the length of each piece
    piece_length = rope_length / total_pieces

    # Display the length of each piece
    result = piece_length
    return result

print(solution())