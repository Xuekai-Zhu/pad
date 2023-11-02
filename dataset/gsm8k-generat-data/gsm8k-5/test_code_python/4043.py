def solution():
    pieces_first_puzzle = 1000  # The first puzzle has 1000 pieces
    pieces_second_puzzle = pieces_first_puzzle * 1.5  # The second puzzle has 50% more pieces than the first
    pieces_third_puzzle = pieces_first_puzzle * 1.5  # The third puzzle has 50% more pieces than the first

    # Calculate the total number of pieces in all three puzzles
    total_pieces = pieces_first_puzzle + pieces_second_puzzle + pieces_third_puzzle
    result = total_pieces
    return result

print(solution())