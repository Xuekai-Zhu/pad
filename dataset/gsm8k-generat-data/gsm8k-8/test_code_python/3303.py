def solution():
    # Define the total number of pages and pages written in the first week
    total_pages = 500
    first_week_pages = 150

    # Calculate the remaining pages after the first week
    remaining_pages = total_pages - first_week_pages

    # Calculate the pages written in the second week
    second_week_pages = 0.3 * remaining_pages

    # Calculate the damaged pages
    damaged_pages = 0.2 * (remaining_pages - second_week_pages)

    # Calculate the total number of empty pages available
    empty_pages = remaining_pages - second_week_pages - damaged_pages
    result = empty_pages
    return result

print(solution())