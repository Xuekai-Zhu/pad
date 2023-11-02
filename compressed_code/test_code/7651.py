def solution():
    
    initial_books = 100
    books_borrowed_first_day = 5 * 2
    books_borrowed_second_day = 20
    remaining_books = initial_books - books_borrowed_first_day - books_borrowed_second_day
    result = remaining_books
    return result

print(solution())