def solution():
    starting_books = 72
    books_from_bookclub = 1 * 12
    books_bought_midyear = 5
    books_bought_yardsales = 2
    books_as_gifts = 1 + 4
    books_donated = 12
    books_sold = 3

    # Calculate the total number of books Mary gained throughout the year
    total_books_gained = books_from_bookclub + books_bought_midyear + books_bought_yardsales + books_as_gifts

    # Calculate the total number of books Mary lost throughout the year
    total_books_lost = books_donated + books_sold

    # Calculate the final number of books Mary has
    final_num_books = starting_books + total_books_gained - total_books_lost
    result = final_num_books
    return result

print(solution())