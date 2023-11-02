def solution():
    """Nancy, the librarian, is shelving books from the cart. She shelved 12 history books, 8 romance books, and 4 poetry books from the top section of the cart. Half the books on the bottom section of the cart were mystery books, which she quickly put back into place. Then, she shelved the remaining books from the bottom of the cart, including 5 Western novels and 6 biographies. How many books did she have on the book cart when she started?"""
    top_shelf_books = 12 + 8 + 4
    bottom_shelf_books = (5 + 6) + (5 + 6)
    total_books = top_shelf_books + bottom_shelf_books
    result = total_books
    return result

print(solution())