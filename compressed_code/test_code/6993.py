def solution():
    
    adult_books = 104
    child_books_percent = 35
    total_books_percent = 100
    child_books = (child_books_percent / total_books_percent) * (adult_books / (1 - (child_books_percent / total_books_percent)))
    total_books = adult_books + child_books
    result = total_books
    return result

print(solution())