def solution():
    
    pieces_per_block = 30
    pieces_per_necklace = 10
    total_pieces = pieces_per_block * 3
    necklaces = total_pieces // pieces_per_necklace
    friends = necklaces - 1 
    result = friends
    return result

print(solution())