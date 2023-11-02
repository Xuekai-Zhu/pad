def solution():
    
    pages_per_day = 10
    total_pages = 200
    days = 30
    pages_read_per_day = pages_per_day * days
    pages_left = total_pages - pages_read_per_day
    days_before_deadline = pages_left / pages_read_per_day
    result = days_before_deadline
    return result

print(solution())