def solution():
    # Calculate the number of pages Coral has left to read after the first week
    remaining_pages = 600/2  # Coral reads half of the book in the first week, so she has 300 pages left

    # Calculate the number of pages Coral reads in the second week
    second_week_pages = remaining_pages * 0.3  # Coral reads 30% of the remaining pages in the second week

    # Calculate the number of pages she has left to read after the second week
    remaining_pages = remaining_pages - second_week_pages

    # Calculate the number of pages she must read in the third week to finish the book
    third_week_pages = remaining_pages / 1  # She needs to finish the remaining pages in one more week

    result = third_week_pages
    return result

print(solution())