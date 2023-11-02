def solution():
    # Define the total number of pages in the book and Joanna's reading speed
    total_pages = 248
    reading_speed = 16

    # Calculate the total number of hours Joanna has read so far
    monday_hours = 3
    tuesday_hours = 6.5
    total_hours = monday_hours + tuesday_hours

    # Calculate the total number of pages Joanna has read so far
    pages_read = total_hours * reading_speed

    # Calculate the number of pages Joanna still needs to read
    pages_left = total_pages - pages_read

    # Calculate the number of hours Joanna still needs to read
    hours_left = pages_left / reading_speed
    result = hours_left
    return result

print(solution())