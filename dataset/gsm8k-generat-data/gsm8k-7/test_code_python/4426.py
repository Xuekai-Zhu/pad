def solution():
    shortest_piece = 16
    ratio = [7, 3, 2]

    # Calculate the total ratio
    total_ratio = sum(ratio)

    # Calculate the length of each piece
    shortest_piece_ratio = ratio[2]
    middle_piece_ratio = ratio[1]
    longest_piece_ratio = ratio[0]

    shortest_piece_length = shortest_piece
    middle_piece_length = shortest_piece * (middle_piece_ratio / shortest_piece_ratio)
    longest_piece_length = shortest_piece * (longest_piece_ratio / shortest_piece_ratio)

    # Calculate the length of the entire wire
    total_length = shortest_piece_length + middle_piece_length + longest_piece_length
    result = total_length
    return result

print(solution())