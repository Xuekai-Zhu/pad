def solution():
    """A library has a collection of 100 historical novels arranged on a shelf. 5 people borrow 2 books each from the shelf on a particular day, and 20 more books are borrowed from the shelf on the second day. How many books are remaining on the shelf after the second day?"""
    total_books = 100
    day_one_borrowing = 5 * 2
    day_two_borrowing = 20
    remaining_books = total_books - day_one_borrowing - day_two_borrowing
    result = remaining_books
    return result

print(solution())