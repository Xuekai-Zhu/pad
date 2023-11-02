def solution():
    """Hadley loves to do volunteer work at the local library. On a certain day, she neatly arranges 100 books on the shelf. By lunchtime, a certain number of books had been borrowed. She added 40 more books to the same shelf. By evening, 30 more books had been borrowed. If the shelf had 60 books remaining by the evening, how many books had been borrowed by lunchtime?"""
    total_books = 100
    books_added = 40
    books_remaining = 60
    books_borrowed = total_books - books_remaining - books_added
    result = books_borrowed
    return result

print(solution())