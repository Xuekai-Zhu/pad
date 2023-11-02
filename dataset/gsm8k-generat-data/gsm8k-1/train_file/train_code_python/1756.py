def solution():
    """Arthur knows that he needs to finish 800 pages of reading over the summer. He has read 80% of a 500-page book and 1/5 of a 1000-page book. How many more pages does he need to reach to meet his goal?"""
    total_pages = 800
    book1_pages = 500
    book1_read = 0.8 * book1_pages
    book2_pages = 1000
    book2_read = book2_pages * (1/5)
    pages_left = total_pages - (book1_read + book2_read)
    result = pages_left
    return result

print(solution())