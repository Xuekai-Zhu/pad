def solution():
    total_pages = 360  # The book has 360 pages
    pages_read_on_saturday = 40  # Ethan read 40 pages on Saturday morning
    pages_read_on_saturday += 10  # Ethan read 10 more pages on Saturday night
    pages_read_on_sunday = 2 * (pages_read_on_saturday)  # Ethan read twice the total pages as on Saturday

    # Calculate the total pages Ethan has read
    total_pages_read = pages_read_on_saturday + pages_read_on_sunday

    # Calculate the pages left to read
    pages_left = total_pages - total_pages_read
    result = pages_left
    return result

print(solution())