def solution():
    
    initial_books = 100
    added_books = 40
    remaining_books = 60
    borrowed_books = initial_books + added_books - remaining_books - 30
    result = borrowed_books
    return result

print(solution())