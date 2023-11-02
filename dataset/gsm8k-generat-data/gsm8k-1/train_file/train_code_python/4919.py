def solution():
    """Erin is sorting through the library books to decide which ones to replace. She finds 8 less than 6 times as many obsolete books as damaged books. If she removes 69 books total, how many books were damaged?"""
    total_removed = 69
    obsolete_books = 6 * damaged_books - 8
    damaged_books = (total_removed + 8) / 7
    result = damaged_books
    return result

print(solution())