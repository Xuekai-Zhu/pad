def solution():
    """Jesse is desperately trying to finish a book for a school book report due on Monday so he can play this weekend. Friday afternoon, he read the first 5 chapters, which were 10, 15, 27, 12, and 19 pages, respectively, before taking a break. To his dismay, he found that he was only 1/3 of the way through the book. How many pages does he still have to read?"""
    pages_read = 10 + 15 + 27 + 12 + 19
    percent_remaining = 2/3
    total_pages = pages_read / (1 - percent_remaining)
    pages_remaining = total_pages - pages_read
    result = pages_remaining
    return result

print(solution())