def solution():
    starting_books = 72
    books_received_from_club = 12  # 1 book per month for 12 months
    books_bought_from_store = 5
    books_bought_from_yard_sales = 2
    books_received_as_gifts = 1 + 4  # 1 from daughter, 4 from mother
    books_donated = 12
    books_sold = 3

    total_books = starting_books + books_received_from_club + books_bought_from_store + \
                  books_bought_from_yard_sales + books_received_as_gifts - books_donated - books_sold

    result = total_books
    return result

print(solution())