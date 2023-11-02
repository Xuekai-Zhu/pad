def solution():
    """James buys 2 puzzles that are 2000 pieces each.  He anticipates for these larger puzzles he can do 100 pieces every 10 minutes.  So how long would it take to finish both puzzles?"""
    # Define the number of puzzles, number of pieces per puzzle, and pieces completed per 10-minute interval
    puzzles = 2
    pieces_per_puzzle = 2000
    pieces_per_interval = 100

    # Calculate the total number of pieces that need to be completed
    total_pieces = puzzles * pieces_per_puzzle

    # Calculate the total number of intervals needed to complete all the puzzles
    total_intervals = total_pieces // pieces_per_interval
    if total_pieces % pieces_per_interval != 0:
        total_intervals += 1

    # Calculate the total time needed to complete all the puzzles
    total_time = total_intervals * 10

    # Display the total time needed to complete both puzzles
    result = total_time
    return result

print(solution())