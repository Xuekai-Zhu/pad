def solution():
    # Darla has 6 books
    darla_books = 6

    # Katie has half as many as Darla
    katie_books = darla_books / 2

    # Gary has 5 times the number of books that Darla and Katie have combined
    gary_books = 5 * (darla_books + katie_books)

    # Total number of books
    total_books = darla_books + katie_books + gary_books
    result = total_books
    return result

print(solution())