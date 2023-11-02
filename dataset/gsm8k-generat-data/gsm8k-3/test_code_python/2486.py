def solution():
    """There are 248 pages in a book. Joanna can read 16 pages per hour. On Monday, she reads for 3 hours. On Tuesday, she reads for 6.5 hours. How many more hours does she need to read to finish the book?"""
    # Define the number of pages in the book and pages Joanna can read per hour
    BOOK_PAGES = 248
    PAGES_PER_HOUR = 16

    # Calculate the total number of hours Joanna has read so far
    hours_read = 3 + 6.5

    # Calculate the total number of pages Joanna has read so far
    pages_read = hours_read * PAGES_PER_HOUR

    # Calculate the remaining number of pages in the book
    pages_remaining = BOOK_PAGES - pages_read

    # Calculate the remaining number of hours needed to finish the book
    hours_remaining = pages_remaining / PAGES_PER_HOUR

    # Display the remaining number of hours needed to finish the book
    result = hours_remaining
    return result

print(solution())