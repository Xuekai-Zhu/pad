def solution():
    """John can read a book 60% faster than his brother. If his brother takes 8 hours to read a book, how long would it take John to read 3 books?"""
    brother_time = 8
    john_speed_increase = 0.6
    john_time = brother_time * (1 - john_speed_increase)
    time_for_3_books = john_time * 3
    result = time_for_3_books
    return result

print(solution())