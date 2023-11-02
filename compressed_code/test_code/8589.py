def solution():
    
    num_books = 3
    days_book1 = 20
    days_book2 = 31
    days_book3 = 31
    fine_per_day = 0.5
    total_fine_book1 = days_book1 * fine_per_day
    total_fine_book2 = days_book2 * fine_per_day
    total_fine_book3 = days_book3 * fine_per_day
    total_fine = total_fine_book1 + total_fine_book2 + total_fine_book3
    result = total_fine
    return result

print(solution())