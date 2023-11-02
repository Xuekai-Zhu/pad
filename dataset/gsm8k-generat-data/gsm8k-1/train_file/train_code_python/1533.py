def solution():
    """A library has a number of books. 35% of them are intended for children and 104 of them are for adults. How many books are in the library?"""
    adult_books = 104
    child_books_percent = 35
    total_books_percent = 100
    child_books = (child_books_percent / total_books_percent) * (adult_books / (1 - (child_books_percent / total_books_percent)))
    total_books = adult_books + child_books
    result = total_books
    return result

print(solution())