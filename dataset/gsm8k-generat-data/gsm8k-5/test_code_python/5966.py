def solution():
    total_pages = 500  # Xander's book has 500 pages
    pages_read_first_night = 0.2 * total_pages  # Xander read 20% of the book on the first night
    pages_read_second_night = 0.2 * total_pages  # Xander read another 20% of the book on the second night
    pages_read_third_night = 0.3 * total_pages  # Xander read 30% of the book on the third night

    # Calculate the total number of pages Xander has left to read
    pages_left = total_pages - (pages_read_first_night + pages_read_second_night + pages_read_third_night)
    result = pages_left
    return result

print(solution())