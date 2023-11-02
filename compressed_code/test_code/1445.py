def solution():
    
    janet_daily_pages = 80
    belinda_daily_pages = 30
    days_in_week = 7
    weeks = 6
    janet_total_pages = janet_daily_pages * days_in_week * weeks
    belinda_total_pages = belinda_daily_pages * days_in_week * weeks
    difference = janet_total_pages - belinda_total_pages
    result = difference
    return result

print(solution())