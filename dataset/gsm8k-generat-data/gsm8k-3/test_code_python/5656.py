def solution():
    """Every day in a week, Siena bookmarks 30 website pages from the research she does on her browser. If Siena has 400 bookmarked pages on her bookmarks library now, how many pages will she have in her bookmarks library at the end of March?"""
    # Find the number of days in March
    days_in_march = 31

    # Find the number of bookmarks Siena adds in a week
    bookmarks_per_week = 30 * 7

    # Find the number of bookmarks Siena adds in March
    bookmarks_in_march = bookmarks_per_week * (days_in_march // 7)

    # Find the total number of bookmarks Siena will have at the end of March
    total_bookmarks = 400 + bookmarks_in_march

    # Display the total number of bookmarks
    result = total_bookmarks
    return result

print(solution())