def solution():
    """A library has a collection of 100 historical novels arranged on a shelf. 5 people borrow 2 books each from the shelf on a particular day, and 20 more books are borrowed from the shelf on the second day. How many books are remaining on the shelf after the second day?"""
    # Define the initial number of books on the shelf
    initial_books = 100

    # Calculate the number of books borrowed on the first day
    books_borrowed_first_day = 5 * 2

    # Calculate the number of books borrowed on the second day
    books_borrowed_second_day = 20

    # Calculate the number of remaining books on the shelf after the second day
    remaining_books = initial_books - books_borrowed_first_day - books_borrowed_second_day

    # Return the result
    result = remaining_books
    return result

print(solution())