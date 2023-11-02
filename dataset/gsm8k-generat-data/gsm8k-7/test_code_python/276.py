def solution():
    total_books = 14
    pages_per_book = 200
    books_read_first_month = 4

    # Calculate the number of books Sabrina has left to read
    books_remaining = total_books - books_read_first_month

    # Calculate the number of books Sabrina will read in the second month
    books_read_second_month = books_remaining / 2

    # Calculate the total number of books Sabrina will read
    total_books_read = books_read_first_month + books_read_second_month

    # Calculate the total number of pages Sabrina has to read to finish the series
    total_pages_to_read = total_books_read * pages_per_book
    result = total_pages_to_read
    return result

print(solution())