def solution():
    bookmarks_per_day = 30
    current_bookmarks = 400
    days_in_march = 31

    # Calculate the total number of bookmarks Siena will add in March
    total_bookmarks_added = bookmarks_per_day * days_in_march

    # Calculate the total number of bookmarks Siena will have at the end of March
    total_bookmarks = current_bookmarks + total_bookmarks_added
    result = total_bookmarks
    return result

print(solution())