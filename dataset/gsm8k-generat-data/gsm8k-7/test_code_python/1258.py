def solution():
    num_books = 15
    puzzles_per_book = 30
    time_per_puzzle = 3

    # Calculate the total number of puzzles in all books
    total_puzzles = num_books * puzzles_per_book

    # Calculate the total time it would take to find every Waldo
    total_time = total_puzzles * time_per_puzzle
    result = total_time
    return result

print(solution())