def solution():
    """If 100 pieces, each 15 centimeters long, are cut from a 51-meter long ribbon, how much ribbon remains ?"""
    ribbon_length = 51
    piece_length = 0.15
    total_piece_length = 100 * piece_length
    remaining_ribbon = ribbon_length - total_piece_length
    result = remaining_ribbon
    return result

print(solution())