def solution():
    """John buys 3 puzzles. The first puzzle has 1000 pieces. The second and third puzzles have the same number of pieces and each has 50% more pieces. How many total pieces are all the puzzles?"""
    first_puzzle = 1000
    second_puzzle = 1.5 * first_puzzle
    third_puzzle = 1.5 * first_puzzle
    total_pieces = first_puzzle + second_puzzle + third_puzzle
    result = total_pieces
    return result

print(solution())