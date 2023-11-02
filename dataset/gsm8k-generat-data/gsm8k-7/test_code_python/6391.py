def solution():
    total_puzzle_pieces = 500
    border_pieces = 75
    trevor_pieces = 105
    joe_pieces = 3 * trevor_pieces
    
    # Calculate the total number of pieces placed by Trevor and Joe
    total_placed = border_pieces + trevor_pieces + joe_pieces
    
    # Calculate the number of pieces missing
    pieces_missing = total_puzzle_pieces - total_placed
    result = pieces_missing
    return result

print(solution())