def solution():
    """Erin is sorting through the library books to decide which ones to replace. She finds 8 less than 6 times as many obsolete books as damaged books. If she removes 69 books total, how many books were damaged?"""
    total_books_removed = 69
    # Let's assume the number of damaged books is x
    # Then the number of obsolete books is 6x - 8
    # According to the problem, the total number of removed books is the sum of damaged and obsolete books
    # So we can write: x + (6x - 8) = total_books_removed
    # Which simplifies to: 7x - 8 = total_books_removed
    # Solving for x, we get:
    damaged_books = (total_books_removed + 8) / 7
    result = damaged_books
    return result

print(solution())