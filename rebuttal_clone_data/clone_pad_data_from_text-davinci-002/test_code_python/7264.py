def solution():
    library_capacity = 400
    current_number_of_books = 120
    target_percentage = 90
    
    number_of_books_needed = library_capacity * ((target_percentage / 100) - (current_number_of_books / library_capacity))
    
    result = number_of_books_needed
    
    return result

print(solution())