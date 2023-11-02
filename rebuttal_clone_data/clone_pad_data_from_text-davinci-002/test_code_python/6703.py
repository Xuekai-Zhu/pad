def solution():
    books_on_wednesday = 98
    books_checked_out_on_wednesday = 43
    books_returned_on_thursday = 23
    books_checked_out_on_thursday = 5
    books_returned_on_friday = 7
    books_on_thursday = books_on_wednesday + books_checked_out_on_wednesday - books_returned_on_thursday
    books_on_friday = books_on_thursday + books_checked_out_on_thursday - books_returned_on_friday
    result = books_on_friday
    return result

print(solution())