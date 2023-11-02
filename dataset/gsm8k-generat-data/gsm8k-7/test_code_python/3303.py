def solution():
    total_pages = 500
    pages_written_week1 = 150
    pages_remaining_week2 = total_pages - pages_written_week1
    pages_written_week2 = int(0.3 * pages_remaining_week2)
    pages_remaining_after_week2 = pages_remaining_week2 - pages_written_week2
    empty_pages_damaged = int(0.2 * pages_remaining_after_week2)
    empty_pages_available = pages_remaining_after_week2 - empty_pages_damaged
    result = empty_pages_available
    return result

print(solution())