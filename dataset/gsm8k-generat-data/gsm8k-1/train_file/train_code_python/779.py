def solution():
    """During one hour, Tom can read 12 pages of a book. How many pages would he be able to read during 2 hours if he could increase his reading speed by a factor of 3?"""
    pages_per_hour = 12
    hours_to_read = 2
    speed_increase_factor = 3
    pages_per_hour *= speed_increase_factor
    total_pages = pages_per_hour * hours_to_read
    result = total_pages
    return result

print(solution())