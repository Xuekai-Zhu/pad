def solution():
    """Joy can read 8 pages of a book in 20 minutes. How many hours will it take her to read 120 pages?"""
    pages_per_minute = 8/20
    pages_to_read = 120
    minutes_to_read = pages_to_read / pages_per_minute
    hours_to_read = minutes_to_read / 60
    result = hours_to_read
    return result

print(solution())