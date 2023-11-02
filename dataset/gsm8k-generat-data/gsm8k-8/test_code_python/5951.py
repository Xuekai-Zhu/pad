def solution():
    total_pages = 158
    pages_read_so_far = 23 + 38 + 61
    pages_left = total_pages - pages_read_so_far
    pages_to_read_on_friday = 2 * pages_to_read_on_thursday

    days_left = 2 # Thursday and Friday
    pages_to_read_per_day = pages_left / days_left

    pages_to_read_on_thursday = (pages_to_read_per_day - pages_to_read_on_friday) / 2

    result = pages_to_read_on_thursday
    return result

print(solution())