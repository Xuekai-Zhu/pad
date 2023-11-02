def solution():
    """John can read a book 60% faster than his brother. If his brother takes 8 hours to read a book, how long would it take John to read 3 books?"""
    brother_time_per_book = 8
    john_time_per_book = brother_time_per_book / 1.6
    total_john_time = john_time_per_book * 3
    result = total_john_time
    return result

print(solution())