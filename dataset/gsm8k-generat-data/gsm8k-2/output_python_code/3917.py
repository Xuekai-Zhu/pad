def solution():
    """Jesse is desperately trying to finish a book for a school book report due on Monday so he can play this weekend.
    Friday afternoon, he read the first 5 chapters, which were 10, 15, 27, 12, and 19 pages, respectively, before taking a break.
    To his dismay, he found that he was only 1/3 of the way through the book. How many pages does he still have to read?"""
    total_pages = sum([10, 15, 27, 12, 19])
    remaining_pages = total_pages * 2
    result = remaining_pages
    return result

print(solution())