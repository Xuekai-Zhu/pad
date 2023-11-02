def solution():
    total_books = 99
    num_weeks = 6

    # Let x be the number of books in the first week
    # Then the number of books in the next five weeks is 10x
    # The total number of books collected is x + 10x = 11x
    # We know that 11x = total_books, so x = total_books/11
    num_first_week_books = total_books / 11

    result = num_first_week_books
    return result

print(solution())