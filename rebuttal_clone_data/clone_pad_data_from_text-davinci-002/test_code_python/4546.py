def solution():
    total_pieces_wood = 672
    pieces_wood_table = 12
    pieces_wood_chair = 8
    tables = total_pieces_wood // pieces_wood_table
    result = (total_pieces_wood - (tables * pieces_wood_table)) // pieces_wood_chair
    return result

print(solution())