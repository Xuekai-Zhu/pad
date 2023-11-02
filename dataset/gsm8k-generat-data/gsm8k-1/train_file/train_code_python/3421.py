def solution():
    """James buys 2 puzzles that are 2000 pieces each. He anticipates for these larger puzzles he can do 100 pieces every 10 minutes. So how long would it take to finish both puzzles?"""
    num_puzzles = 2
    pieces_per_puzzle = 2000
    time_per_100_pieces = 10
    total_pieces = num_puzzles * pieces_per_puzzle
    time_in_minutes = (total_pieces / 100) * time_per_100_pieces
    result = time_in_minutes
    return result

print(solution())