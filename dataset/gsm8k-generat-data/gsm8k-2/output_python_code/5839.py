def solution():
    """Phil has 10 books that are all 100 pages each. He moves to a new home and during the move, 2 books are lost. How many pages worth of books does Phil have left?"""
    num_books = 10
    lost_books = 2
    pages_per_book = 100
    remaining_books = num_books - lost_books
    total_pages = remaining_books * pages_per_book
    result = total_pages
    return result

print(solution())