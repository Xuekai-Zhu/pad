def solution():
    
    initial_books = 235
    tuesday_books = 227
    thursday_books_back = 56
    friday_books = 35
    total_books = initial_books - tuesday_books + thursday_books_back - friday_books
    result = total_books
    return result

print(solution())