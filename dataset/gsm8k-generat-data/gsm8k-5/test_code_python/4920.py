def solution():
    obsolete_books = 6 * damaged_books - 8  # Erin finds 8 less than 6 times as many obsolete books as damaged books
    total_books = obsolete_books + damaged_books  # The total number of books is the sum of obsolete and damaged books
    removed_books = 69  # Erin removes 69 books in total

    # Calculate the number of damaged books
    damaged_books = (total_books - removed_books) / 2

    result = damaged_books
    return result

print(solution())