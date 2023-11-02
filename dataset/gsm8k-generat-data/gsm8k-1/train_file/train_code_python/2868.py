def solution():
    """The new pad of paper has 120 pages. Sammy uses 25% of the pages for his science project,
    and another 10 pages for his math homework. How many pages remain in the pad?"""
    total_pages = 120
    science_pages = total_pages * 0.25
    math_pages = 10
    remaining_pages = total_pages - science_pages - math_pages
    result = remaining_pages
    return result

print(solution())