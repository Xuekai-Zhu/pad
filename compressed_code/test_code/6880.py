def solution():
    
    total_books = 54
    initial_books = 6 + 3
    remaining_books = total_books - initial_books
    books_per_week = 9
    weeks_to_read = remaining_books / books_per_week + 2
    result = weeks_to_read
    return result

print(solution())