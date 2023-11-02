def solution():
    
    total_pages = 140
    pages_per_day_initial = 3 * 6
    days_to_finish = 7
    pages_per_day_needed = total_pages / days_to_finish
    pages_extra_per_day = pages_per_day_needed - pages_per_day_initial
    result = pages_extra_per_day
    return result

print(solution())