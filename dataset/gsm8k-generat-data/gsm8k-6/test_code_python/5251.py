def solution():
    # Calculate the number of pieces of cake Donna had left after the party
    leftovers = 0.5 * 0.5  # guests ate half the cake, which left Donna with half of the cake, which was halved with her brothers
    # Calculate the number of pieces left after Donna's midnight snack
    pieces_left = 2 * (leftovers - 1)  # twice as many pieces as her midnight snack were left
    # Calculate the number of pieces the cake was to begin with
    total_pieces = pieces_left + 1  # Donna ate one piece as a midnight snack, so there were (pieces_left + 1) pieces to start with
    result = total_pieces
    return result

print(solution())