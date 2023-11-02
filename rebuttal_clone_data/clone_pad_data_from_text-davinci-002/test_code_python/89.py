def solution():
    """Krystian works in the library. He borrows an average of 40 books every day. Every Friday, his number of borrowed books is about 40% higher than the daily average. How many books does he borrow in a week if the library is open from Monday to Friday?"""
    daily_average = 40
    percent_increase = 40
    books_borrowed_on_friday = daily_average + (daily_average * (percent_increase / 100))
    books_borrowed_other_days = daily_average
    total_books_borrowed = books_borrowed_on_friday + (books_borrowed_other_days * 4)
    result = total_books_borrowed
    return result

print(solution())