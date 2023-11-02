def solution():
    """Every bedtime, Juwella reads a book. Three nights ago, she read 15 pages. Two nights ago she read twice that many pages, 
    while last night she read 5 pages more than the previous night. She promised to read the remaining pages of the book tonight. 
    If the book has 100 pages, how many pages will she read tonight?"""
    # Define the total number of pages in the book
    total_pages = 100

    # Calculate the number of pages Juwella read in the past three nights
    pages_read = 15 + 2 * 15 + (2 * 15 + 5)

    # Calculate the number of pages remaining to be read
    pages_remaining = total_pages - pages_read

    # return the result
    result = pages_remaining
    return result

print(solution())