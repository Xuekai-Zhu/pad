def solution():
    num_puzzles = 3
    pieces_first_puzzle = 1000
    pieces_second_puzzle = pieces_first_puzzle * 1.5
    pieces_third_puzzle = pieces_first_puzzle * 1.5
    
    # Calculate the total number of pieces in all puzzles
    total_pieces = (pieces_first_puzzle + pieces_second_puzzle + pieces_third_puzzle) * num_puzzles
    result = total_pieces
    return result

print(solution())