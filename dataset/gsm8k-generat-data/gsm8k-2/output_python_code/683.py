def solution():
    """Grace can read a 200-page book in 20 hours. How long would it take her to finish reading a 250-page book at this constant rate?"""
    # Grace can read 200 pages in 20 hours, so her reading rate is 200/20 = 10 pages per hour
    # To read a 250-page book at this rate, it would take Grace 250/10 = 25 hours
    pages_in_book = 250
    pages_per_hour = 10
    reading_time = pages_in_book / pages_per_hour
    result = reading_time
    return result

print(solution())