def solution():
    """John writes 20 pages a day. How long will it take him to write 3 books that are 400 pages each?"""
    pages_per_day = 20
    total_pages = 3 * 400
    days_needed = total_pages / pages_per_day
    result = days_needed
    return result

print(solution())