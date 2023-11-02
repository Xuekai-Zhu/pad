def solution():
    
    total_pieces = 100
    pieces_per_level = 7
    leftover_pieces = 23
    used_pieces = total_pieces - leftover_pieces
    levels = used_pieces // pieces_per_level
    result = levels
    return result

print(solution())