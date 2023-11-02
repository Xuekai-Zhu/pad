def solution():
    """Cody was reading through his favorite book series. The series was 54 books in total. If Cody read 6 books the first week, and 3 books the second week and then 9 books every week after that. How many weeks did it take Cody to read his series?"""
    total_books = 54
    initial_books = 6 + 3
    remaining_books = total_books - initial_books
    books_per_week = 9
    weeks_to_read = remaining_books / books_per_week + 2
    result = weeks_to_read
    return result

print(solution())