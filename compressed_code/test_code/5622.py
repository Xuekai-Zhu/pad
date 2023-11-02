def solution():
    
    total_pieces = 60
    michael_pieces = total_pieces // 2
    remainder1 = total_pieces - michael_pieces
    paige_pieces = remainder1 // 2
    remainder2 = remainder1 - paige_pieces
    mandy_pieces = remainder2
    result = mandy_pieces
    return result

print(solution())