def solution():
    """Jamal works at a library shelving books. He has a cart full of books to put away in different sections. In the history section, he shelves 12 books. In the fiction section, he shelves 19 books. In the children’s section, he shelves 8 books but finds 4 that were left in the wrong place that he adds to his cart to shelve elsewhere. He still has 16 books to shelve. How many books did he start with in the cart?"""
    books_history = 12
    books_fiction = 19
    books_children = 8
    books_found = 4
    books_remaining = 16
    total_books = books_history + books_fiction + books_children + books_found + books_remaining
    result = total_books
    return result

print(solution())