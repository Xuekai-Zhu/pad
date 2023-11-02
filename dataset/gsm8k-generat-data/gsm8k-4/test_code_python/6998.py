def solution():
    """Jo reads at a steady pace. Her current book has 210 pages. Now, she is at page 90. An hour ago, she was at page 60. For how many hours will she be reading the book?"""
    # Define the total number of pages in the book
    total_pages = 210

    # Calculate the number of pages Jo has left to read
    pages_left = total_pages - 90

    # Calculate the number of pages Jo read in the past hour
    pages_read_in_past_hour = 90 - 60

    # Calculate Jo's reading speed in pages per hour
    speed = pages_read_in_past_hour

    # Calculate the number of hours Jo will need to finish the book
    hours_needed = pages_left / speed

    result = hours_needed
    return result

print(solution())