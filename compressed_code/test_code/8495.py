def solution():
    
    num_puzzles = 2
    pieces_per_puzzle = 2000
    time_per_100_pieces = 10
    total_pieces = num_puzzles * pieces_per_puzzle
    time_in_minutes = (total_pieces / 100) * time_per_100_pieces
    result = time_in_minutes
    return result

print(solution())