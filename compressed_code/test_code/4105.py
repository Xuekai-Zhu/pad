def solution():
    
    total_pieces = 240
    eaten_pieces = total_pieces * 0.6
    remaining_pieces = total_pieces - eaten_pieces
    pieces_per_sister = remaining_pieces / 3
    result = pieces_per_sister
    return result

print(solution())