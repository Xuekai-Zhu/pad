def solution():
    """Jamal works at a library shelving books. He has a cart full of books to put away in different sections. In the history section, he shelves 12 books. In the fiction section, he shelves 19 books. In the children’s section, he shelves 8 books but finds 4 that were left in the wrong place that he adds to his cart to shelve elsewhere. He still has 16 books to shelve. How many books did he start with in the cart?"""
    history_books = 12
    fiction_books = 19
    children_books = 8 + 4
    remaining_books = 16
    total_books = history_books + fiction_books + children_books + remaining_books
    result = total_books
    return result

print(solution())