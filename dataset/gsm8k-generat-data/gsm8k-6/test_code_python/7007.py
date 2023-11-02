def solution():
    # Calculate the number of levels in Jade's lego tower
    remaining_pieces = 23
    pieces_per_level = 7
    levels = (100 - remaining_pieces) // pieces_per_level
    result = levels
    return result

print(solution())