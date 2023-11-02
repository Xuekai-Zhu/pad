def solution():
    """A library has a number of books. 35% of them are intended for children and 104 of them are for adults. How many books are in the library?"""
    adult_books = 104
    child_books_percentage = 0.35
    total_percentage = 1

    # Solve for child books
    child_books_percentage = total_percentage - child_books_percentage
    child_books = child_books_percentage * (adult_books / 0.65)

    # Solve for total books
    total_books = adult_books + child_books
    result = total_books
    return result

print(solution())