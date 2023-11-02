def solution():
    # Find the number of books Katie has
    katie_books = 6/2 

    # Find the total number of books Darla and Katie have combined
    darla_katie_books = 6 + katie_books 

    # Find the total number of books Gary has
    gary_books = 5 * darla_katie_books

    # Find the total number of books the three have
    total_books = darla_katie_books + gary_books
    result = total_books
    return result

print(solution())