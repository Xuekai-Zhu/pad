def solution():
    pages_per_day = 3 * 6
    desired_pages = 140
    days_in_week = 7
    pages_needed = desired_pages - (pages_per_day * days_in_week)
    result = pages_needed
    
    return result

print(solution())