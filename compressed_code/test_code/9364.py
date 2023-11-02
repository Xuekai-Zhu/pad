def solution():
    
    pieces_of_wood = 672
    pieces_per_table = 12
    pieces_per_chair = 8
    total_pieces_for_tables = pieces_per_table * 24
    pieces_left = pieces_of_wood - total_pieces_for_tables
    chairs = pieces_left // pieces_per_chair
    result = chairs
    
    return result

print(solution())