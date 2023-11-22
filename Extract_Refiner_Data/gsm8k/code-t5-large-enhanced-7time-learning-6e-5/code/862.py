def solution():
    
    total_books = 85
    anne_books = (total_books + 12) / 2
    sofie_books = anne_books + 25
    fawn_books = total_books - anne_books - sofie_books
    result = fawn_books
    return result

print(solution())