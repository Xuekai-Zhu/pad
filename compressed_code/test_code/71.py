def solution():
    
    daily_average = 40
    friday_increase = 0.4
    friday_books = daily_average * (1 + friday_increase)
    weekly_books = (daily_average * 4) + friday_books
    result = weekly_books
    return result

print(solution())