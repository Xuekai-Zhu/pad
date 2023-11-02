def solution():
    """Erin is sorting through the library books to decide which ones to replace. She finds 8 less than 6 times as many obsolete books as damaged books. If she removes 69 books total, how many books were damaged?"""
    # Let's assume the number of damaged books is x
    x = 0

    # Calculate the number of obsolete books using the given relationship
    obsolete_books = 6 * x - 8

    # Calculate the total number of removed books
    total_removed_books = x + obsolete_books

    # Iterate over possible values of x until we find the one that satisfies the total_removed_books requirement
    while total_removed_books != 69:
        x += 1
        obsolete_books = 6 * x - 8
        total_removed_books = x + obsolete_books

    # The remaining value of x will be the number of damaged books
    result = x
    return result

print(solution())