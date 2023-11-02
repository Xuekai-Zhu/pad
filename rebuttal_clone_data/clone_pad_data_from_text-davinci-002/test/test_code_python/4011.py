def solution():
    books_borrowed = 5
    books_returned = 3
    books_checked_out = 5
    books_returned2 = 2
    books_checked_out2 = 7
    books_outstanding = books_borrowed + books_checked_out - books_returned - books_returned2 + books_checked_out2
    result =  books_outstanding
    return result

print(solution())