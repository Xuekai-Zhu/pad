def solution():
    """Amalia can read 4 pages of her book in 2 minutes. How many minutes will it take her to read 18 pages of her book?"""
    # Define the reading speed
    speed = 4 / 2  # pages per minute

    # Define the number of pages to read
    pages_to_read = 18

    # Calculate the time needed to read the pages
    time_needed = pages_to_read / speed  # minutes

    # return the result
    result = time_needed
    return result

print(solution())