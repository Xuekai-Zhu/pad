def solution():
    """Rich is reading a 372-page book. He has already read 125 pages of the book. If he skipped the 16 pages of maps, how many more pages does he have left to read to finish the book?"""
    # Define the total number of pages in the book, and the number of pages read and skipped
    total_pages = 372
    pages_read = 125
    pages_skipped = 16

    # Calculate the number of pages left to read
    pages_left = total_pages - pages_read - pages_skipped

    # return the result
    result = pages_left
    return result

print(solution())