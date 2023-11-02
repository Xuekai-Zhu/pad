def solution():
    
    total_pieces = 500
    border_pieces = 75
    trevor_pieces = 105
    joe_pieces = 3 * trevor_pieces
    placed_pieces = border_pieces + trevor_pieces + joe_pieces
    missing_pieces = total_pieces - placed_pieces
    result = missing_pieces
    return result

print(solution())