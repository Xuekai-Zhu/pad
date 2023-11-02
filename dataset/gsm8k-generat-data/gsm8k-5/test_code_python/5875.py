def solution():
    blank_pages_lana = 8  # Lana had 8 blank pages left in her binder
    pages_duane = 42  # Duane had 42 pages in his binder
    pages_given = pages_duane / 2  # Duane gave half of his pages to Lana

    # Calculate the total number of pages Lana has in her binder
    total_pages = blank_pages_lana + pages_given
    result = total_pages
    return result

print(solution())