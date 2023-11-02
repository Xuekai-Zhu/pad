def solution():
    """Darla has 6 books in her locker. Katie has half as many books as Darla, and Gary has 5 times the number of books that Darla and Katie have combined. How many books do the three have total?"""
    darla_books = 6
    katie_books = darla_books / 2
    combined_books = darla_books + katie_books
    gary_books = 5 * combined_books
    total_books = darla_books + katie_books + gary_books
    result = total_books
    return result

print(solution())