def solution():
    # Calculate the current number of old books in the library
    old_books = 500 + 200  # 200 old books were donated this year

    # Calculate the current number of new books in the library
    new_books_last_year = 300
    new_books_this_year = new_books_last_year + 100
    new_books = new_books_last_year + new_books_this_year

    # Calculate the total number of books in the library now
    total_books = old_books + new_books
    result = total_books
    return result

print(solution())