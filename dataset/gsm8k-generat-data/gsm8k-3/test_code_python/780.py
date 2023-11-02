def solution():
    """During one hour, Tom can read 12 pages of a book. How many pages would he be able to read during 2 hours if he could increase his reading speed by a factor of 3?"""
    # Define Tom's reading speed in pages per hour
    TOM_SPEED = 12

    # Define the number of hours Tom will read
    hours = 2

    # Define the factor by which Tom's reading speed will increase
    factor = 3

    # Calculate Tom's increased reading speed
    increased_speed = TOM_SPEED * factor

    # Calculate the total number of pages Tom can read in 2 hours
    total_pages = increased_speed * hours

    # Display the total number of pages Tom can read in 2 hours
    result = total_pages
    return result

print(solution())