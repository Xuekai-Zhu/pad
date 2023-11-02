def solution():
    """Nancy, the librarian, is shelving books from the cart. She shelved 12 history books, 8 romance books, and 4 poetry books from the top section of the cart. Half the books on the bottom section of the cart were mystery books, which she quickly put back into place. Then, she shelved the remaining books from the bottom of the cart, including 5 Western novels and 6 biographies. How many books did she have on the book cart when she started?"""
    top_history_books = 12
    top_romance_books = 8
    top_poetry_books = 4
    bottom_mystery_books = 0.5 * (top_history_books + top_romance_books + top_poetry_books)
    bottom_western_books = 5
    bottom_biography_books = 6
    total_books = top_history_books + top_romance_books + top_poetry_books + bottom_mystery_books + bottom_western_books + bottom_biography_books
    result = total_books
    return result

print(solution())