def solution():
    """John buys 3 puzzles.  The first puzzle has 1000 pieces.  The second and third puzzles have the same number of pieces and each has 50% more pieces.  How many total pieces are all the puzzles?"""
    # Define the number of pieces in the first puzzle
    puzzle1 = 1000

    # Calculate the number of pieces in the second and third puzzles
    puzzle2 = puzzle1 * 1.5
    puzzle3 = puzzle1 * 1.5

    # Calculate the total number of pieces in all the puzzles
    total_pieces = puzzle1 + puzzle2 + puzzle3

    # Display the total number of pieces
    result = total_pieces
    return result

print(solution())