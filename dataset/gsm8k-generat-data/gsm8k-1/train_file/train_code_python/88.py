def solution():
    """Krystian works in the library. He borrows an average of 40 books every day. Every Friday, his number of borrowed books is about 40% higher than the daily average. How many books does he borrow in a week if the library is open from Monday to Friday?"""
    daily_average = 40
    friday_increase = 0.4
    friday_borrowed = daily_average * (1 + friday_increase)
    total_borrowed = daily_average * 4 + friday_borrowed
    result = total_borrowed
    return result

print(solution())