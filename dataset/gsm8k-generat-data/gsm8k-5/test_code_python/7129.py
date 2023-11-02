def solution():
    # Mary initially borrowed 5 books
    books_checked_out = 5

    # Mary returns 3 unhelpful books and checks out 5 new ones
    books_checked_out = books_checked_out - 3 + 5

    # Mary returns 2 books and checks out 7 more
    books_checked_out = books_checked_out - 2 + 7

    result = books_checked_out
    return result

print(solution())