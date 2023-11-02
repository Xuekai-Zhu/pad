def solution():
    
    daily_average = 40
    percent_increase = 40
    books_borrowed_on_friday = daily_average + (daily_average * (percent_increase / 100))
    books_borrowed_other_days = daily_average
    total_books_borrowed = books_borrowed_on_friday + (books_borrowed_other_days * 4)
    result = total_books_borrowed
    return result

print(solution())