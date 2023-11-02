def solution():
    
    total_pages = 248
    pages_per_hour = 16
    monday_hours = 3
    tuesday_hours = 6.5
    pages_read = (monday_hours + tuesday_hours) * pages_per_hour
    remaining_pages = total_pages - pages_read
    hours_to_finish = remaining_pages / pages_per_hour
    result = hours_to_finish
    return result

print(solution())