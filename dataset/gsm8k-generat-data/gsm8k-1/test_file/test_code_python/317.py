def solution():
    """A magazine costs half as much as a book. The book costs $4. A pen costs $1 less than a magazine. How much is the pen?"""
    book_cost = 4
    magazine_cost = book_cost / 2
    pen_cost = magazine_cost - 1
    result = pen_cost
    return result

print(solution())