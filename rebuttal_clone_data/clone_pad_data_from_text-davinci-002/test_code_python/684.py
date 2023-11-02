def solution():
    pages_read = 200
    hours_needed = 20
    new_pages = 250
    new_hours = new_pages / (pages_read / hours_needed)
    result = new_hours
    return result

print(solution())