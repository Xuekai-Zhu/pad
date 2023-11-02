def solution():
    """Lance wants to finish reading a 100 page book in 3 days. Yesterday, he started to read 35 pages. Today, he read 5 fewer pages than yesterday. How many pages should he read tomorrow to finish the book?"""
    total_pages = 100
    days_left = 3 - 2  # He has already finished 2 days of reading
    pages_per_day = (total_pages - 35 - (35 - 5)) / days_left
    result = pages_per_day
    return result

print(solution())