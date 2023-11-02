def solution():
    """There have been 15 "Where's Waldo?" books published. Each book has 30 puzzles to find Waldo. The average person takes 3 minutes to find Waldo in a puzzle. How long would it take to find every Waldo?"""
    num_books = 15
    puzzles_per_book = 30
    time_per_puzzle = 3  # in minutes
    total_puzzles = num_books * puzzles_per_book
    total_time = total_puzzles * time_per_puzzle  # in minutes
    result = total_time
    return result

print(solution())