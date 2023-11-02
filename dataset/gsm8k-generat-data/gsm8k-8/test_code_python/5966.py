def solution():
    # Define the total number of pages in the book
    total_pages = 500

    # Calculate the number of pages Xander read on the first night
    pages_read_first_night = total_pages * 0.2

    # Calculate the number of pages Xander read on the second night
    pages_read_second_night = total_pages * 0.2

    # Calculate the number of pages Xander read on the third night
    pages_read_third_night = total_pages * 0.3

    # Calculate the total number of pages Xander has left to read
    pages_left = total_pages - pages_read_first_night - pages_read_second_night - pages_read_third_night

    result = pages_left
    return result

print(solution())