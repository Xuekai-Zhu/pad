def solution():
    """Every bedtime, Juwella reads a book. Three nights ago, she read 15 pages. Two nights ago she read twice that many pages, while last night she read 5 pages more than the previous night. She promised to read the remaining pages of the book tonight. If the book has 100 pages, how many pages will she read tonight?"""
    book_pages = 100
    three_nights_ago_pages = 15
    two_nights_ago_pages = 2 * three_nights_ago_pages
    last_night_pages = two_nights_ago_pages + 5
    total_read_pages = three_nights_ago_pages + two_nights_ago_pages + last_night_pages
    remaining_pages = book_pages - total_read_pages
    result = remaining_pages
    return result

print(solution())