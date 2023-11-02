def solution():
    total_pages = 360
    saturday_morning_pages = 40
    saturday_night_pages = 10
    sunday_pages = (saturday_morning_pages + saturday_night_pages) * 2

    # Calculate the total pages that Ethan has read so far
    total_read_pages = saturday_morning_pages + saturday_night_pages + sunday_pages

    # Calculate the pages that Ethan has left to read
    pages_left = total_pages - total_read_pages
    result = pages_left
    return result

print(solution())