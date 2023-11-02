def solution():
    
    weekdays = 5
    weekend_days = 2
    weekday_pages = 10
    weekend_pages = 20
    total_weekdays = weekdays * 2
    total_weekend_days = weekend_days * 2
    total_pages = (total_weekdays * weekday_pages) + (total_weekend_days * weekend_pages)
    result = total_pages
    return result

print(solution())