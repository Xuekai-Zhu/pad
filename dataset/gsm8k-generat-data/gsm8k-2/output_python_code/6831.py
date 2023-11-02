def solution():
    """The time Juan takes to grab his lunch from his office and back is half the time he takes to read a book. If he has a 4000-page book, how many pages does he read in an hour if he takes 4 hours to move from his office to grab lunch?"""
    lunch_time = 4
    book_time = 2 * lunch_time
    book_pages = 4000
    pages_per_hour = book_pages / book_time
    result = pages_per_hour
    return result

print(solution())