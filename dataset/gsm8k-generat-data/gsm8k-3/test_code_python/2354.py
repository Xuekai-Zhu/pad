def solution():
    """A library has a collection of 100 historical novels arranged on a shelf. 5 people borrow 2 books each from the shelf on a particular day,
     and 20 more books are borrowed from the shelf on the second day. How many books are remaining on the shelf after the second day?"""
    # Define the initial number of books on the shelf
    INITIAL_BOOKS = 100

    # Calculate the number of books borrowed on the first day
    first_day_borrowed = 5 * 2

    # Calculate the total number of books borrowed after the second day
    total_borrowed = first_day_borrowed + 20

    # Calculate the number of books remaining on the shelf
    remaining_books = INITIAL_BOOKS - total_borrowed

    # Display the number of books remaining
    result = remaining_books
    return result

print(solution())