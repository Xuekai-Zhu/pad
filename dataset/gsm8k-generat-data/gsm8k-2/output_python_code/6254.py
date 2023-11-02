def solution():
    """Rich is reading a 372-page book. He has already read 125 pages of the book. If he skipped the 16 pages of maps, how many more pages does he have left to read to finish the book?"""
    total_pages = 372
    pages_read = 125
    map_pages = 16
    remaining_pages = total_pages - pages_read - map_pages
    result = remaining_pages
    return result

print(solution())