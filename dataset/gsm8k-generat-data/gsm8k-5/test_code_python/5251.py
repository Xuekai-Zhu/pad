def solution():
    # Calculate the number of pieces left after the party
    remaining_after_party = 0.5

    # Calculate the number of pieces left after sharing with brothers
    remaining_after_brothers = remaining_after_party * 0.5

    # Calculate the number of pieces left before Donna ate a piece
    remaining_before_snack = remaining_after_brothers * 2

    # Calculate the total number of pieces to begin with
    total_pieces = remaining_before_snack + 1
    result = total_pieces
    return result

print(solution())