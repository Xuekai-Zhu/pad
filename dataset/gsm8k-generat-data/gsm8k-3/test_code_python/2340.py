def solution():
    """Jamal works at a library shelving books. He has a cart full of books to put away in different sections. In the history section, he shelves 12 books. In the fiction section, he shelves 19 books. In the children’s section, he shelves 8 books but finds 4 that were left in the wrong place that he adds to his cart to shelve elsewhere. He still has 16 books to shelve. How many books did he start with in the cart?"""
    # Define the number of books Jamal shelve in each section
    history_books = 12
    fiction_books = 19
    children_books = 8
    misplaced_books = 4

    # Calculate the total number of books Jamal shelve
    shelve_books = history_books + fiction_books + children_books + misplaced_books

    # Calculate the number of books Jamal started with in the cart
    initial_books = shelve_books + 16

    # Display the initial number of books in the cart
    result = initial_books
    return result

print(solution())