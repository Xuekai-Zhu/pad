def solution():
    """Every bedtime, Juwella reads a book. Three nights ago, she read 15 pages. Two nights ago she read twice that many pages, while last night she read 5 pages more than the previous night. She promised to read the remaining pages of the book tonight. If the book has 100 pages, how many pages will she read tonight?"""
    total_pages = 100
    pages_read_first_night = 15
    pages_read_second_night = 2 * pages_read_first_night
    pages_read_third_night = pages_read_second_night + 5
    pages_read_so_far = pages_read_first_night + pages_read_second_night + pages_read_third_night
    pages_left_to_read = total_pages - pages_read_so_far
    result = pages_left_to_read
    return result

print(solution())