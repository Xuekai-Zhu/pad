def solution():
    """Joy can read 8 pages of a book in 20 minutes. How many hours will it take her to read 120 pages?"""
    pages_per_minute = 8/20
    minutes_to_read_120_pages = 120 / pages_per_minute
    hours_to_read_120_pages = minutes_to_read_120_pages / 60
    result = hours_to_read_120_pages
    return result

print(solution())