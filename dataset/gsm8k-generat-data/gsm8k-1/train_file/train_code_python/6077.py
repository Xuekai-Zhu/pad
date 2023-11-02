def solution():
    """Cyrus has been contracted to write a 500 page book. On his first day, he writes 25 pages and twice that amount on the second day. On the third day he is able to write twice the amount that he did on the second day. On the fourth day, he gets writer's block and is only able to write 10 pages. How many more pages does he need to write?"""
    total_pages = 500
    day1_pages = 25
    day2_pages = day1_pages * 2
    day3_pages = day2_pages * 2
    day4_pages = 10
    total_written = day1_pages + day2_pages + day3_pages + day4_pages
    pages_left = total_pages - total_written
    result = pages_left
    return result

print(solution())