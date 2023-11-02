def solution():
    bookmarks_per_day = 30  # Siena bookmarks 30 pages per day
    start_pages = 400  # Siena has 400 pages bookmarked already
    days_in_march = 31  # There are 31 days in March

    # Calculate the total number of bookmarks Siena will add in March
    total_bookmarks = bookmarks_per_day * days_in_march

    # Calculate the total number of bookmarks Siena will have in her library at the end of March
    final_bookmarks = start_pages + total_bookmarks
    result = final_bookmarks
    return result

print(solution())