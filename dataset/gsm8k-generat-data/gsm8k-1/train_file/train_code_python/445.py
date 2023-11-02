def solution():
    """In a classroom, 10 children have 7 books each. Their teacher brings another 8 books to the classroom. How many books are in the classroom altogether?"""
    children = 10
    initial_books = 7
    extra_books = 8
    total_books = children * initial_books + extra_books
    result = total_books
    return result

print(solution())