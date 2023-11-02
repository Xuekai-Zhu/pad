def solution():
    """During one hour, Tom can read 12 pages of a book. How many pages would he be able to read during 2 hours if he could increase his reading speed by a factor of 3?"""
    # Define the reading speed and time variables
    reading_speed = 12 * 3
    time = 2

    # Calculate the total number of pages he can read
    total_pages = reading_speed * time

    # return the result
    result = total_pages
    return result

print(solution())