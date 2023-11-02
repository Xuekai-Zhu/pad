def solution():
    """James buys 2 puzzles that are 2000 pieces each. He anticipates for these larger puzzles he can do 100 pieces every 10 minutes. So how long would it take to finish both puzzles?"""
    puzzle_size = 2000
    pieces_completed_per_10_minutes = 100
    time_per_10_minutes = 10
    total_pieces = puzzle_size * 2
    total_time_in_minutes = (total_pieces / pieces_completed_per_10_minutes) * time_per_10_minutes
    result = total_time_in_minutes
    return result

print(solution())