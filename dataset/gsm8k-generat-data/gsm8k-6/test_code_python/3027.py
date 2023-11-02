def solution():
    # Calculate the total number of books Mary has at the end of the year
    mystery_books = 72
    books_from_bookclub = 12  # Mary received 1 book per month
    books_from_bookstore = 5
    books_from_yardsales = 2
    books_gifted = 1 + 4  # one from daughter and four from mother
    books_donated = 12
    books_sold = 3

    total_books = mystery_books + books_from_bookclub + books_from_bookstore + books_from_yardsales + books_gifted
    total_books -= books_donated + books_sold  # subtract the books donated and sold
    result = total_books
    return result

print(solution())