def solution():

    initial_book_count = 990
    percent_of_books_left = 60
    books_left = initial_book_count * (percent_of_books_left / 100)
    books_sold = initial_book_count - books_left
    result = books_sold

    return result

print(solution())