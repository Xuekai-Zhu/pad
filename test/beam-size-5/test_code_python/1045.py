def solution():
    
    total_books = 50
    english_books = total_books / 2
    german_books = total_books * 0.1
    Spanish_books = total_books - english_books - german_books
    result = Spanish_books
    return result

print(solution())