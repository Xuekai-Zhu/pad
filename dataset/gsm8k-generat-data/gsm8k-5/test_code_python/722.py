def solution():
    total_pages = 600  # Coral's book is 600 pages long
    pages_read_first_week = total_pages / 2  # Coral reads half of the book in the first week
    pages_remaining = total_pages - pages_read_first_week  # Coral has this many pages left to read
    pages_read_second_week = pages_remaining * 0.3  # Coral reads 30% of the remaining pages in the second week
    pages_left = pages_remaining - pages_read_second_week  # Coral has this many pages left to read
    pages_to_read_third_week = pages_left / 1  # Coral needs to read the rest of the pages in the third week

    result = pages_to_read_third_week
    return result

print(solution())