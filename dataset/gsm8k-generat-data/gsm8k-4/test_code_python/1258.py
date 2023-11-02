def solution():
    """There have been 15 "Where's Waldo?" books published. Each book has 30 puzzles to find Waldo. The average person takes 3 minutes to find Waldo in a puzzle. How long would it take to find every Waldo?"""
    # Define the number of books, puzzles, and time to find Waldo
    NUM_BOOKS = 15
    PUZZLES_PER_BOOK = 30
    MINUTES_PER_PUZZLE = 3

    # Calculate the total number of puzzles
    total_puzzles = NUM_BOOKS * PUZZLES_PER_BOOK

    # Calculate the total time to find every Waldo
    total_time = total_puzzles * MINUTES_PER_PUZZLE

    # return the result
    result = total_time
    return result

print(solution())