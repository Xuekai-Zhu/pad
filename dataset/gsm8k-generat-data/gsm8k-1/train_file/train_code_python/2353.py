def solution():
    """A library has a collection of 100 historical novels arranged on a shelf. 5 people borrow 2 books each from the shelf on a particular day, and 20 more books are borrowed from the shelf on the second day. How many books are remaining on the shelf after the second day?"""
    initial_books = 100
    books_borrowed_first_day = 5 * 2
    books_borrowed_second_day = 20
    remaining_books = initial_books - books_borrowed_first_day - books_borrowed_second_day
    result = remaining_books
    return result

print(solution())