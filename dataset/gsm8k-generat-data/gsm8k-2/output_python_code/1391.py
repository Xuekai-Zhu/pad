def solution():
    """Cody was reading through his favorite book series. The series was 54 books in total. If Cody read 6 books the first week, and 3 books the second week and then 9 books every week after that. How many weeks did it take Cody to read his series?"""
    total_books = 54
    first_week_books = 6
    second_week_books = 3
    remaining_books = total_books - first_week_books - second_week_books
    weekly_books = 9
    weeks_to_finish = remaining_books / weekly_books + 2
    result = weeks_to_finish
    return result

print(solution())