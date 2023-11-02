def solution():
    
    library_capacity = 400
    current_books = 120
    target_percent = 0.9
    target_books = library_capacity * target_percent
    additional_books = target_books - current_books
    result = additional_books
    return result

print(solution())