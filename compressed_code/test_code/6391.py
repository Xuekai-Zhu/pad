def solution():
    
    pages_per_hour = 12
    hours_to_read = 2
    speed_increase_factor = 3
    pages_per_hour *= speed_increase_factor
    total_pages = pages_per_hour * hours_to_read
    result = total_pages
    return result

print(solution())