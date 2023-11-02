def solution():
    """Bill started reading a book on the first day of April. He read 8 pages every day and by the 12th of April, he had covered two-thirds of the book. How many pages does the book have?"""
    days_read = 12
    pages_per_day = 8
    percent_covered = 2/3
    pages_covered = days_read * pages_per_day * percent_covered
    total_pages = pages_covered / (percent_covered)
    result = total_pages
    return result

print(solution())