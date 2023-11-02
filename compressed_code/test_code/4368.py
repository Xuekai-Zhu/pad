def solution():
    
    days_in_march = 31
    pages_bookmarked_per_day = 30
    current_pages = 400
    total_pages = current_pages + (days_in_march * pages_bookmarked_per_day)
    result = total_pages
    return result

print(solution())