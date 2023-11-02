def solution():
    """Nancy, the librarian, is shelving books from the cart. She shelved 12 history books, 8 romance books, and 4 poetry books from the top section of the cart. Half the books on the bottom section of the cart were mystery books, which she quickly put back into place. Then, she shelved the remaining books from the bottom of the cart, including 5 Western novels and 6 biographies. How many books did she have on the book cart when she started?"""
    # Calculate the number of books shelved from the top section of the cart
    top_books = 12 + 8 + 4

    # Calculate the number of mystery books on the bottom section of the cart
    bottom_mystery = top_books / 2

    # Calculate the number of books shelved from the bottom section of the cart
    bottom_books = 5 + 6 + bottom_mystery

    # Calculate the total number of books on the cart
    total_books = top_books + bottom_books

    # return the result
    result = total_books
    return result

print(solution())