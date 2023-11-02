def solution():
    
    total_books = 54
    first_week_books = 6
    second_week_books = 3
    remaining_books = total_books - first_week_books - second_week_books
    weekly_books = 9
    weeks_to_finish = remaining_books / weekly_books + 2
    result = weeks_to_finish
    return result

print(solution())