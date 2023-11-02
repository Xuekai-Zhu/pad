def solution():
    """Carter can read half as many pages as Lucy in 1 hour. Lucy can read 20 more pages than Oliver in 1 hour. Oliver can read 40 pages. How many pages can Carter read in 1 hour?"""
    oliver_pages = 40
    lucy_pages = oliver_pages + 20
    carter_pages = lucy_pages / 2
    result = carter_pages
    return result

print(solution())