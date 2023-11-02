def solution():
    """Xander read 20% of his 500-page book in one hour.  The next night he read another 20% of the book.  On the third night, he read 30% of his book.  How many pages does he have left to read?"""
    # Define the total number of pages in the book
    TOTAL_PAGES = 500

    # Calculate the number of pages Xander read on the first night
    pages_read_1 = TOTAL_PAGES * 0.2

    # Calculate the number of pages Xander read on the second night
    pages_read_2 = TOTAL_PAGES * 0.2

    # Calculate the number of pages Xander read on the third night
    pages_read_3 = TOTAL_PAGES * 0.3

    # Calculate the total number of pages Xander read
    pages_read_total = pages_read_1 + pages_read_2 + pages_read_3

    # Calculate the number of pages Xander has left to read
    pages_left = TOTAL_PAGES - pages_read_total

    # Display the number of pages Xander has left to read
    result = pages_left
    return result

print(solution())