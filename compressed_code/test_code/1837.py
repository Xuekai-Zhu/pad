def solution():
    
    total_books = 100
    day_one_borrowing = 5 * 2
    day_two_borrowing = 20
    remaining_books = total_books - day_one_borrowing - day_two_borrowing
    result = remaining_books
    return result

print(solution())