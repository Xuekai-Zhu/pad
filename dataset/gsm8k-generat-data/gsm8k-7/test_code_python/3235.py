def solution():
    total_pages = 93
    saturday_pages = 30
    sunday_pages = 20

    # Calculate the total number of pages read by Jerry
    total_read = saturday_pages + sunday_pages

    # Calculate the number of remaining pages
    remaining_pages = total_pages - total_read
    result = remaining_pages
    return result

print(solution())