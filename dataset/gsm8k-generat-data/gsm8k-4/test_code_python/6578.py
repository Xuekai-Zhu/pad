def solution():
    """The library has 9,900 books. Over the summer, they sold some books. If only four sixths of the books are left, how many did they sell?"""
    # Define the initial number of books and the remaining fraction
    initial_books = 9900
    remaining_fraction = 4/6

    # Calculate the number of books sold
    books_sold = initial_books - initial_books * remaining_fraction

    result = books_sold
    return result

print(solution())