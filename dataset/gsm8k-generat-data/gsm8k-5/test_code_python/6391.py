def solution():
    total_pieces = 500  # The puzzle has 500 pieces
    border_pieces = 75  # The border has 75 pieces
    trevor_pieces = 105  # Trevor placed 105 puzzle pieces
    joe_pieces = 3 * trevor_pieces  # Joe placed three times as many pieces as Trevor

    # Calculate the total number of pieces placed
    total_placed = border_pieces + trevor_pieces + joe_pieces

    # Calculate the number of missing pieces
    missing_pieces = total_pieces - total_placed
    result = missing_pieces
    return result

print(solution())