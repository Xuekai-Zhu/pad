def solution():
    history_pages = 160
    geography_pages = history_pages + 70
    math_pages = (history_pages + geography_pages) / 2
    science_pages = 2 * history_pages

    # Calculate the total number of pages in all textbooks
    total_pages = history_pages + geography_pages + math_pages + science_pages
    result = total_pages
    return result

print(solution())