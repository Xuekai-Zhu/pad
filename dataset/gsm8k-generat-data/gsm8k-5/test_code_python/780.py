def solution():
    pages_per_hour = 12  # Tom can read 12 pages in one hour
    increased_speed = 3  # Tom can increase his reading speed by a factor of 3
    new_speed = pages_per_hour * increased_speed  # Calculate Tom's new reading speed
    hours = 2  # Tom wants to read for 2 hours

    # Calculate the total number of pages Tom can read in 2 hours with the increased speed
    total_pages = new_speed * hours
    result = total_pages
    return result

print(solution())