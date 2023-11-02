def solution():
    
    total_books = 336
    monday_books = 124
    tuesday_books = 22
    remaining_books = total_books - monday_books + tuesday_books
    result = remaining_books
    return result

print(solution())