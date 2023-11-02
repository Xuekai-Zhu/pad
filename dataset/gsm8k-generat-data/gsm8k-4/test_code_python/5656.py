def solution():
    """Every day in a week, Siena bookmarks 30 website pages from the research she does on her browser. If Siena has 400 bookmarked pages on her bookmarks library now, how many pages will she have in her bookmarks library at the end of March?"""
    # Define the initial number of bookmarked pages
    initial_bookmarks = 400

    # Calculate the number of bookmarked pages per day
    daily_bookmarks = 30

    # Calculate the number of days in March
    days_in_march = 31

    # Calculate the total number of bookmarked pages at the end of March
    total_bookmarks = initial_bookmarks + (daily_bookmarks * days_in_march)

    # return the result
    result = total_bookmarks
    return result

print(solution())