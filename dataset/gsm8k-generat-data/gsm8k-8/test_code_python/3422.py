def solution():
    # Define the number of puzzles and the number of pieces per puzzle
    num_puzzles = 2
    pieces_per_puzzle = 2000

    # Calculate the total number of pieces
    total_pieces = num_puzzles * pieces_per_puzzle

    # Calculate the number of minutes needed to complete all the puzzles
    minutes_needed = (total_pieces / 100) * 10

    result = minutes_needed
    return result

print(solution())