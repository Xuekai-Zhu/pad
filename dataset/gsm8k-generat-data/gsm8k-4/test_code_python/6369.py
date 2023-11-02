def solution():
    """A rope has a length of 200 meters. Stefan cuts the rope into four equal parts, gives his mother half of the cut pieces, and subdivides the remaining pieces into two more equal parts. What's the length of each piece?"""
    # Define the initial length of the rope
    rope_length = 200

    # Calculate the length of each of the four equal pieces
    equal_piece_length = rope_length / 4

    # Calculate the number of pieces given to Stefan's mother
    mother_pieces = 2

    # Calculate the number of remaining pieces
    remaining_pieces = 4 - mother_pieces

    # Calculate the length of each of the remaining pieces
    remaining_piece_length = equal_piece_length / 2

    # Calculate the total number of remaining pieces
    total_remaining_pieces = remaining_pieces * 2

    # Calculate the final length of each piece
    final_length = remaining_piece_length

    result = final_length
    return result

print(solution())