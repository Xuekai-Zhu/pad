def solution():
    """Sabrina went to the library and found a historical series novel called The Rangers Apprentice. There are 14 books in the series, and each book has 200 pages. She read four books in a month and half the number of books remaining in the second month. What's the total number of pages Sabrina has to read to finish the whole series?"""
    # Define the total number of books in the series and the number of pages per book
    total_books = 14
    pages_per_book = 200

    # Calculate the total number of pages in the series
    total_pages = total_books * pages_per_book

    # Calculate the number of books Sabrina has already read
    books_read = 4

    # Calculate the number of books remaining
    books_remaining = total_books - books_read

    # Calculate the number of books Sabrina will read in the second month
    books_second_month = books_remaining // 2

    # Calculate the total number of pages Sabrina has to read to finish the whole series
    pages_to_read = (books_remaining - books_second_month) * pages_per_book

    # return the result
    result = pages_to_read
    return result

print(solution())