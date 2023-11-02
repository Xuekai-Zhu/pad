def solution():
    # Calculate the pieces left after the party
    pieces_left_after_party = 0.5

    # Calculate the pieces left after sharing with her brothers
    pieces_left_after_sharing = 0.5 * pieces_left_after_party

    # Calculate the pieces left after Donna's midnight snack
    pieces_left_after_snack = 2 * (pieces_left_after_sharing - 1)

    # Calculate the total pieces of cake to begin with
    total_pieces = pieces_left_after_snack + 1
    result = total_pieces
    return result

print(solution())