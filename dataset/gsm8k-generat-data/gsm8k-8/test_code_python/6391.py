def solution():
    total_pieces = 500
    border_pieces = 75
    trevor_pieces = 105
    joe_pieces = 3 * trevor_pieces

    # Calculate the total pieces placed by both Trevor and Joe
    total_placed = border_pieces + trevor_pieces + joe_pieces

    # Calculate the pieces missing to complete the puzzle
    pieces_missing = total_pieces - total_placed
    result = pieces_missing
    return result

print(solution())