def solution():
    """Darla has 6 books in her locker. Katie has half as many books as Darla, and Gary has 5 times the number of books that Darla and Katie have combined. How many books do the three have total?"""

    # Define the number of books Darla has
    darla_books = 6

    # Calculate the number of books Katie has
    katie_books = darla_books / 2

    # Calculate the total number of books Darla and Katie have combined
    total_darla_katie_books = darla_books + katie_books

    # Calculate the number of books Gary has
    gary_books = 5 * total_darla_katie_books

    # Calculate the total number of books the three have
    total_books = darla_books + katie_books + gary_books

    # Return the result
    result = total_books
    return result

print(solution())