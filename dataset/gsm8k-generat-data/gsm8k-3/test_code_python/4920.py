def solution():
    """Erin is sorting through the library books to decide which ones to replace. She finds 8 less than 6 times as many obsolete books as damaged books. If she removes 69 books total, how many books were damaged?"""
    # Let's assume the number of damaged books to be x
    # Then the number of obsolete books is 6x - 8

    # Total number of removed books is 69
    # So, x + (6x - 8) = 69
    # Solving for x, we get x = 11

    # Therefore the number of damaged books is 11
    result = 11
    return result

print(solution())