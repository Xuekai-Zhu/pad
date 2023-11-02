def solution():
    """Every day in a week, Siena bookmarks 30 website pages from the research she does on her browser. 
    If Siena has 400 bookmarked pages on her bookmarks library now, how many pages will she have in her bookmarks library at the end of March?"""
    days_in_march = 31
    pages_bookmarked_per_day = 30
    current_pages = 400
    total_pages = current_pages + (days_in_march * pages_bookmarked_per_day)
    result = total_pages
    return result

print(solution())