def solution():
    """Alex is stacking his books in a pyramid. Each level of the pyramid has 80% as many books as the number of books in the previous level. If he makes four levels and the top level has 64 books, how many books are in the pyramid in total?"""
    top_level_books = 64
    level_three_books = top_level_books / 0.8
    level_two_books = level_three_books / 0.8
    level_one_books = level_two_books / 0.8
    total_books = top_level_books + level_three_books + level_two_books + level_one_books
    result = total_books
    return result

print(solution())