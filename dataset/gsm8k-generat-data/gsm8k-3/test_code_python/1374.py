def solution():
    """Darla has 6 books in her locker.  Katie has half as many books as Darla, and Gary has 5 times the number of books that Darla and Katie have combined.  How many books do the three have total?"""
    # Define Darla's number of books
    darla_books = 6

    # Calculate Katie's number of books
    katie_books = darla_books / 2

    # Calculate the combined number of books Darla and Katie have
    darla_katie_books = darla_books + katie_books

    # Calculate Gary's number of books
    gary_books = 5 * darla_katie_books

    # Calculate the total number of books the three have
    total_books = darla_books + katie_books + gary_books

    # Display the total number of books
    result = total_books
    return result

print(solution())