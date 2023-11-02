def solution():
    """Grace can read a 200-page book in 20 hours. How long would it take her to finish reading a 250-page book at this constant rate?"""
    pages_per_hour = 200 / 20
    hours_to_read_250_pages = 250 / pages_per_hour
    result = hours_to_read_250_pages
    return result

print(solution())