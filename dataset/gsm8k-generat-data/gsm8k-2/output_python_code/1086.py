def solution():
    """Hadley loves to do volunteer work at the local library. On a certain day, she neatly arranges 100 books on the shelf. By lunchtime, a certain number of books had been borrowed. She added 40 more books to the same shelf. By evening, 30 more books had been borrowed. If the shelf had 60 books remaining by the evening, how many books had been borrowed by lunchtime?"""
    initial_books = 100
    added_books = 40
    remaining_books = 60
    borrowed_books = initial_books + added_books - remaining_books - 30
    result = borrowed_books
    return result

print(solution())