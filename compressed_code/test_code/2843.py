def solution():
    
    book_pages = 100
    three_nights_ago_pages = 15
    two_nights_ago_pages = 2 * three_nights_ago_pages
    last_night_pages = two_nights_ago_pages + 5
    total_read_pages = three_nights_ago_pages + two_nights_ago_pages + last_night_pages
    remaining_pages = book_pages - total_read_pages
    result = remaining_pages
    return result

print(solution())