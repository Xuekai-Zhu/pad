def solution():
    old_books_five_years_ago = 500
    books_bought_two_years_ago = 300
    books_bought_last_year = books_bought_two_years_ago + 100
    books_donated_this_year = 200

    # Calculate the total number of books bought in the past three years
    total_books_bought = books_bought_two_years_ago + books_bought_last_year

    # Calculate the current number of books in the library
    current_books = old_books_five_years_ago + total_books_bought - books_donated_this_year
    result = current_books
    return result

print(solution())