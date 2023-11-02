def solution():
    purple_pages = 230
    orange_pages = 510
    purple_books = 5
    orange_books = 4

    # Calculate the total number of purple pages read
    total_purple_pages = purple_pages * purple_books

    # Calculate the total number of orange pages read
    total_orange_pages = orange_pages * orange_books

    # Calculate the difference between orange pages and purple pages
    difference = total_orange_pages - total_purple_pages
    result = difference
    return result

print(solution())