def solution():
    rope_length = 200  # The rope has a length of 200 meters
    num_pieces = 4  # Stefan cuts the rope into 4 equal parts

    # Calculate the length of each piece before giving half to his mother
    piece_length_before = rope_length / num_pieces

    # Stefan gives half of the cut pieces to his mother
    pieces_to_keep = num_pieces / 2
    pieces_to_give = num_pieces - pieces_to_keep

    # Calculate the length of each piece after giving half to his mother
    piece_length_after = piece_length_before * pieces_to_keep / pieces_to_give

    # Stefan subdivides the remaining pieces into two equal parts
    pieces_remaining = num_pieces - pieces_to_keep
    final_piece_length = piece_length_after / 2

    result = final_piece_length
    return result

print(solution())