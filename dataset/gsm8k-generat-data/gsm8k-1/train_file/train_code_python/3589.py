def solution():
    """Hallie borrows a book from the library. She reads the entire book in four days. She read 63 pages the first day. On the second day, she read twice the number of pages that she'd read on day one. On the third day, she read 10 mores pages than she read on day two. If the book is 354 pages long, how many pages did she read on the fourth day?"""
    total_pages = 354
    day1_pages = 63
    day2_pages = day1_pages * 2
    day3_pages = day2_pages + 10
    pages_read_so_far = day1_pages + day2_pages + day3_pages
    day4_pages = total_pages - pages_read_so_far
    result = day4_pages
    return result

print(solution())