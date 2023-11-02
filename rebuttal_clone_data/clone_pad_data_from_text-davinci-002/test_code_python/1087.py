def solution():
    morning_arrangement = 100
    evening_arrangement = 60
    total_books_borrowed = morning_arrangement - evening_arrangement
    lunchtime_borrowed = total_books_borrowed - 30
    result = lunchtime_borrowed
    return result

print(solution())