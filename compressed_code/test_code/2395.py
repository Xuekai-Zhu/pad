def solution():
    
    initial_donations = 300
    new_donations = 10 * 5
    borrowed_books = 140
    remaining_books = initial_donations + new_donations - borrowed_books
    result = remaining_books
    return result

print(solution())