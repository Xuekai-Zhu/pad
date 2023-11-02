def solution():
    """Bill started reading a book on the first day of April. He read 8 pages every day and by the 12th of April, he had covered two-thirds of the book. How many pages does the book have?"""
    pages_read = 8 * 11  # 8 pages a day for 11 days (April 1-11)
    percent_read = 2/3
    total_pages = pages_read / percent_read
    result = total_pages
    return result

print(solution())