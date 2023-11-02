def solution():
    
    total_pieces = 1000
    pieces_placed_on_board = total_pieces / 4
    pieces_remaining = total_pieces - pieces_placed_on_board
    pieces_placed_on_mom = pieces_remaining / 3
    pieces_left = pieces_remaining - pieces_placed_on_mom
    result = pieces_left
    return result

print(solution())