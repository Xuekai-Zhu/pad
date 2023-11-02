def solution():
    num_books = 15  # There have been 15 "Where's Waldo?" books published
    puzzles_per_book = 30  # Each book has 30 puzzles to find Waldo
    time_per_puzzle = 3  # The average person takes 3 minutes to find Waldo in a puzzle

    # Calculate the total number of puzzles and the total time needed to find every Waldo
    total_puzzles = num_books * puzzles_per_book
    total_time = total_puzzles * time_per_puzzle

    result = total_time
    return result

print(solution())