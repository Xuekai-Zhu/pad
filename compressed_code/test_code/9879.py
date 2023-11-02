def solution():
    
    total_pieces = 60
    swept_pieces = total_pieces / 2
    stolen_pieces = 3
    remaining_pieces = total_pieces - swept_pieces - stolen_pieces
    boyfriend_pieces = remaining_pieces / 3
    result = boyfriend_pieces
    return result

print(solution())