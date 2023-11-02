def solution():
    initial_pages = 500
    pages_used = 150
    pages_left = initial_pages - pages_used
    pages_written_second_week = pages_left * 0.3
    pages_left = pages_left - pages_written_second_week
    pages_spilled_on = pages_left * 0.2
    total_pages_left = pages_left - pages_spilled_on
    result = total_pages_left
    return result

print(solution())