def solution():
    
    total_pages = 210
    current_page = 90
    pages_read_in_one_hour = current_page - 60
    hours_needed = (total_pages - current_page) / pages_read_in_one_hour
    result = hours_needed
    return result

print(solution())