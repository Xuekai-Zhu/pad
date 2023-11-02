def solution():
    old_books_5_years_ago = 500
    books_bought_2_years_ago = 300
    books_bought_last_year = books_bought_2_years_ago + 100
    books_donated_this_year = 200
    total_books = old_books_5_years_ago + books_bought_2_years_ago + books_bought_last_year - books_donated_this_year
    result = total_books
    return result

print(solution())