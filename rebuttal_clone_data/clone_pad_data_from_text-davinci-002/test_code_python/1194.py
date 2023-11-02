def solution():
    inches_rope = 72
    pieces_cut = 12
    knots = 3
    length_each_piece = (inches_rope - knots) / pieces_cut
    result = length_each_piece
    return result

print(solution())