def solution():
    """Jo reads at a steady pace. Her current book has 210 pages. Now, she is at page 90. An hour ago, she was at page 60. For how many hours will she be reading the book?"""
    total_pages = 210
    current_page = 90
    pages_read = current_page - 60
    pages_left = total_pages - current_page
    hours_needed = pages_left / pages_read
    result = hours_needed
    return result

print(solution())