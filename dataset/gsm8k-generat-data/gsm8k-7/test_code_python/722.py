def solution():
    total_pages = 600
    first_week_pages = total_pages / 2
    remaining_pages = total_pages - first_week_pages
    second_week_pages = remaining_pages * 0.3
    pages_left = remaining_pages - second_week_pages
    pages_to_read_third_week = pages_left / 1
    result = pages_to_read_third_week
    return result

print(solution())