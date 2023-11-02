def solution():
    """Every bedtime, Juwella reads a book. Three nights ago, she read 15 pages. Two nights ago she read twice that many pages, while last night she read 5 pages more than the previous night. She promised to read the remaining pages of the book tonight. If the book has 100 pages, how many pages will she read tonight?"""
    # Define the number of pages Juwella read on each night
    night1 = 15
    night2 = night1 * 2
    night3 = night2 + 5

    # Calculate the total number of pages Juwella has read so far
    total_pages_read = night1 + night2 + night3

    # Calculate the number of pages left in the book
    pages_left = 100 - total_pages_read

    # Display the number of pages Juwella will read tonight
    result = pages_left
    return result

print(solution())