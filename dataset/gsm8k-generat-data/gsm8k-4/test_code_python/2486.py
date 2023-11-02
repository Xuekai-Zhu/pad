def solution():
    """There are 248 pages in a book. Joanna can read 16 pages per hour. On Monday, she reads for 3 hours. On Tuesday, she reads for 6.5 hours. How many more hours does she need to read to finish the book?"""
    # Define the total number of pages and the reading speed
    total_pages = 248
    reading_speed = 16

    # Calculate the total number of hours already spent reading
    hours_read = 3 + 6.5

    # Calculate the total number of pages already read
    pages_read = hours_read * reading_speed

    # Calculate the number of pages yet to be read
    pages_left = total_pages - pages_read

    # Calculate the hours needed to finish the book
    hours_needed = pages_left / reading_speed

    # Return the result
    result = hours_needed
    return result

print(solution())