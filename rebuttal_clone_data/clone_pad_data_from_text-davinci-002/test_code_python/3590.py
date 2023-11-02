def solution():
    pages_read_1 = 63
    pages_read_2 = pages_read_1 * 2
    pages_read_3 = pages_read_2 + 10
    total_pages = 354
    pages_read_4 = total_pages - (pages_read_1 + pages_read_2 + pages_read_3)
    result = pages_read_4
    return result

print(solution())