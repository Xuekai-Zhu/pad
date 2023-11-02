def solution():
    """Steve decides to read a new book. He reads 100 pages Monday, Wed, and Friday. The book is 2100 pages long. How many weeks does it take to read them all?"""
    pages_per_week = 300  # 100 pages per day, 3 days a week
    book_length = 2100
    weeks_to_read = book_length / pages_per_week
    result = weeks_to_read
    return result

print(solution())