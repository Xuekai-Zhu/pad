def solution():
    # Define the length of the book and the pages already read
    total_pages = 600
    first_week_pages = total_pages / 2

    # Calculate the remaining pages and the pages read in the second week
    remaining_pages = total_pages - first_week_pages
    second_week_pages = 0.3 * remaining_pages

    # Calculate the pages left to be read and the pages to be read in the third week
    pages_left = total_pages - first_week_pages - second_week_pages
    third_week_pages = pages_left / 1
    result = third_week_pages
    return result

print(solution())