def solution():
    """During one hour, Tom can read 12 pages of a book. How many pages would he be able to read during 2 hours if he could increase his reading speed by a factor of 3?"""
    pages_per_hour = 12
    increased_speed = 3 * pages_per_hour
    time = 2
    pages = increased_speed * time
    result = pages
    return result

print(solution())