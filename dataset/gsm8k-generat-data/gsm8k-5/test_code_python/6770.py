def solution():
    old_books_five_years_ago = 500  # Five years ago, there were 500 old books in the library
    current_old_books = old_books_five_years_ago  # The current number of old books is the same as the number five years ago
    books_bought_two_years_ago = 300  # Two years ago, the librarian bought 300 books
    books_bought_last_year = books_bought_two_years_ago + 100  # Last year, the librarian bought 100 more books than the previous year
    books_donated_this_year = 200  # This year, the librarian donated 200 of the old books

    # Calculate the current number of books in the library
    current_books = current_old_books + books_bought_two_years_ago + books_bought_last_year - books_donated_this_year
    result = current_books
    return result

print(solution())