def solution():
    pieces_per_hour = 100
    max_hours_per_day = 7

    num_small_puzzles = 8
    small_puzzle_pieces = 300

    num_large_puzzles = 5
    large_puzzle_pieces = 500

    # Calculate the total number of pieces in all of the puzzles
    total_pieces = (num_small_puzzles * small_puzzle_pieces) + (num_large_puzzles * large_puzzle_pieces)

    # Calculate the total number of hours it will take to complete all the puzzles
    total_hours = total_pieces / pieces_per_hour

    # Calculate the number of days it will take to complete all the puzzles
    num_days = total_hours / max_hours_per_day
    result = num_days
    return result

print(solution())