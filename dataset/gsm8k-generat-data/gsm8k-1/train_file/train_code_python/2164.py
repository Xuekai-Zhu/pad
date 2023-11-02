def solution():
    """There are 381 pages in Elliot’s book. He has already read 149 pages. If he reads 20 pages a day for a week, how many pages are still left to be read?"""
    total_pages = 381
    pages_read = 149
    pages_per_day = 20
    days_in_week = 7
    pages_left = total_pages - pages_read - (pages_per_day * days_in_week)
    result = pages_left
    return result

print(solution())