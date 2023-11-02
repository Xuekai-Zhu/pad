def solution():
    # Calculate total reading time in hours
    total_reading_time = 24 * (1/6)

    # Calculate time spent on each type of book
    time_per_book = total_reading_time / 3

    # Calculate pages read for each type of book
    pages_per_novel = time_per_book * 21
    pages_per_graphic_novel = time_per_book * 30
    pages_per_comic_book = time_per_book * 45

    # Calculate total pages read
    total_pages_read = pages_per_novel + pages_per_graphic_novel + pages_per_comic_book
    result = total_pages_read
    return result

print(solution())