def solution():
    """Tracy has been collecting novels from her friends to donate to the Children For The Future charity organization. In the first week she collects a certain number of books. In the next five weeks, she collects ten times as many books as she did in the first week. How many books did she collect in the first week if she has 99 books now?"""
    total_books = 99
    first_week_books = x
    next_five_weeks_books = 10 * first_week_books
    total_books_collected = first_week_books + next_five_weeks_books
    total_weeks = 6  # including the first week
    average_books_per_week = total_books_collected / total_weeks
    x = total_books / average_books_per_week
    result = x
    return result

print(solution())