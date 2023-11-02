def solution():
    # Let x be the number of damaged books
    # Then the number of obsolete books is 6x - 8
    # The total number of removed books is x + (6x - 8) = 7x - 8

    total_removed = 69
    obsolete_books = 6 * x - 8

    # We know that the total_removed is the sum of damaged_books and obsolete_books
    # So we can set up the equation:

    x + (6x - 8) = total_removed

    # Solving for x:

    7x - 8 = total_removed
    7x = total_removed + 8
    x = (total_removed + 8) / 7

    damaged_books = x
    result = damaged_books
    return result

print(solution())