def solution():
    """Nancy, the librarian, is shelving books from the cart. She shelved 12 history books, 8 romance books, and 4 poetry books from the top section of the cart. Half the books on the bottom section of the cart were mystery books, which she quickly put back into place. Then, she shelved the remaining books from the bottom of the cart, including 5 Western novels and 6 biographies. How many books did she have on the book cart when she started?"""
    
    top_history = 12
    top_romance = 8
    top_poetry = 4
    bottom_mystery = 2 * top_romance
    bottom_western = 5
    bottom_biography = 6
    
    total_books = top_history + top_romance + top_poetry + bottom_mystery + bottom_western + bottom_biography
    
    result = total_books
    return result

print(solution())