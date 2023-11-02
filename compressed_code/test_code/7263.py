def solution():
    
    janet_pages_per_day = 80
    belinda_pages_per_day = 30
    days_per_week = 7
    weeks = 6
    janet_total_pages = janet_pages_per_day * days_per_week * weeks
    belinda_total_pages = belinda_pages_per_day * days_per_week * weeks
    difference = janet_total_pages - belinda_total_pages
    result = difference
    return result

print(solution())