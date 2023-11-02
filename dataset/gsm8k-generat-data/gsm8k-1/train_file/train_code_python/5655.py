def solution():
    """Every day in a week, Siena bookmarks 30 website pages. If she has 400 bookmarked pages now, how many pages will she have at the end of March?"""
    bookmarks_per_week = 30 * 7
    current_bookmarks = 400
    total_bookmarks = current_bookmarks + (bookmarks_per_week * 4)
    result = total_bookmarks
    return result

print(solution())