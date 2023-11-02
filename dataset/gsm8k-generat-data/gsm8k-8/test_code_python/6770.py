def solution():
    # Calculate the number of old books currently in the library
    old_books_now = 500

    # Calculate the number of books the librarian bought two years ago
    books_bought_two_years_ago = 300

    # Calculate the number of books the librarian bought last year
    books_bought_last_year = books_bought_two_years_ago + 100

    # Calculate the total number of books in the library before any books were donated this year
    total_books_before_donation = old_books_now + books_bought_two_years_ago + books_bought_last_year

    # Calculate the total number of books in the library after the donation this year
    total_books_now = total_books_before_donation - 200
    result = total_books_now
    return result

print(solution())