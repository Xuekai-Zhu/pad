def solution():
    """Phil has 10 books that are all 100 pages each. He moves to a new home and during the move, 2 books are lost. How many pages worth of books does Phil have left?"""
    num_books = 10
    pages_per_book = 100
    books_lost = 2
    pages_left = (num_books - books_lost) * pages_per_book
    result = pages_left
    return result

print(solution())