def solution():
    pieces = 100
    length_per_piece = 15
    total_length_cut = pieces * length_per_piece
    ribbon_length = 51
    remaining_ribbon = ribbon_length - total_length_cut
    result = remaining_ribbon
    return result

print(solution())