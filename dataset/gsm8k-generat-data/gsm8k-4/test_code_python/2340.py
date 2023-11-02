def solution():
    """Jamal works at a library shelving books. He has a cart full of books to put away in different sections. In the history section, he shelves 12 books. In the fiction section, he shelves 19 books. In the children’s section, he shelves 8 books but finds 4 that were left in the wrong place that he adds to his cart to shelve elsewhere. He still has 16 books to shelve. How many books did he start with in the cart?"""
    # Calculate the total number of books Jamal shelve
    total_shelved = 12 + 19 + 8 + 4

    # Calculate the number of books left to shelve
    books_left = 16

    # Calculate the initial number of books in the cart
    initial_books = total_shelved + books_left

    # Return the result
    result = initial_books
    return result

print(solution())