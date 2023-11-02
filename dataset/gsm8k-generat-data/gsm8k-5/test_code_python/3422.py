def solution():
    pieces_per_puzzle = 2000  # Each puzzle has 2000 pieces
    total_puzzles = 2  # James is buying 2 puzzles
    pieces_per_minute = 10  # James can complete 100 pieces in 10 minutes

    # Calculate the total number of pieces James needs to complete
    total_pieces = pieces_per_puzzle * total_puzzles

    # Calculate the total time it will take James to complete both puzzles
    total_time = (total_pieces / 100) * 10  # James can complete 100 pieces in 10 minutes

    result = total_time
    return result

print(solution())