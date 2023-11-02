def solution():
    """Tracy used a piece of wire 4 feet long to support tomato plants in the garden. The wire was cut into pieces 6 inches long. How many pieces did she obtain?"""
    total_length_inches = 4 * 12
    length_per_piece = 6
    total_pieces = total_length_inches // length_per_piece
    result = total_pieces
    return result

print(solution())