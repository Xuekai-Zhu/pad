def solution():
    total_pages_goal = 800
    pages_read_book1 = 0.8 * 500
    pages_read_book2 = 0.2 * 1000
    pages_read_total = pages_read_book1 + pages_read_book2
    pages_left = total_pages_goal - pages_read_total
    result = pages_left
    return result

print(solution())