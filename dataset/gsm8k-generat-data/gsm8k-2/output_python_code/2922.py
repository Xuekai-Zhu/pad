def solution():
    """Ruel has four books of 10 stamps and six books of 15 stamps. How many stamps does Ruel have?"""
    num_books_10 = 4
    num_books_15 = 6
    stamps_per_book_10 = 10
    stamps_per_book_15 = 15
    total_stamps_10 = num_books_10 * stamps_per_book_10
    total_stamps_15 = num_books_15 * stamps_per_book_15
    total_stamps = total_stamps_10 + total_stamps_15
    result = total_stamps
    return result

print(solution())