def solution():
    rope_length = 200
    num_parts = 4

    # Calculate the length of each cut piece
    cut_piece_length = rope_length / num_parts

    # Calculate the number of pieces given to Stefan's mother
    num_pieces_for_mother = num_parts / 2

    # Calculate the length of each piece given to Stefan's mother
    length_for_mother = num_pieces_for_mother * cut_piece_length

    # Calculate the remaining pieces
    remaining_pieces = num_parts - num_pieces_for_mother

    # Divide the remaining pieces into two equal parts
    num_final_pieces = remaining_pieces * 2

    # Calculate the length of each final piece
    final_piece_length = rope_length / num_final_pieces

    result = final_piece_length
    return result

print(solution())