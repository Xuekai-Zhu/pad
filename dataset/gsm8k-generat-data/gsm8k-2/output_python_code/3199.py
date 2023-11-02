def solution():
    """If 100 pieces, each 15 centimeters long, are cut from a 51-meter long ribbon, how much ribbon remains?"""
    total_cut_length = 100 * 0.15
    remaining_length = 51 - total_cut_length
    result = remaining_length
    return result

print(solution())