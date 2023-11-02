def solution():
    total_pages = 248
    pages_per_hour = 16
    hours_read_on_monday = 3
    hours_read_on_tuesday = 6.5
    pages_read_on_monday = pages_per_hour * hours_read_on_monday
    pages_read_on_tuesday = pages_per_hour * hours_read_on_tuesday
    pages_left_to_read = total_pages - (pages_read_on_monday + pages_read_on_tuesday)
    hours_left_to_read = pages_left_to_read / pages_per_hour
    result = hours_left_to_read
    return result

print(solution())