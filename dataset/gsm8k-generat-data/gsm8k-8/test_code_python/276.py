def solution():
    # Define the total number of books and pages per book
    num_books = 14
    pages_per_book = 200

    # Calculate the number of books Sabrina has left to read
    books_remaining = num_books - 4

    # Calculate the number of books Sabrina read in the second month
    second_month_books = books_remaining / 2

    # Calculate the total number of books Sabrina will read
    total_books = 4 + second_month_books

    # Calculate the total number of pages Sabrina has to read
    total_pages = total_books * pages_per_book
    result = total_pages
    return result

print(solution())