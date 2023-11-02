def solution():
    """Nate is reading a 400-page book. He finished reading 20% of the book. How many pages does he need to read to finish the book?"""
    # Define the number of pages in the book
    TOTAL_PAGES = 400

    # Calculate the number of pages Nate has already read
    pages_read = TOTAL_PAGES * 0.2

    # Calculate the number of pages Nate still needs to read
    pages_left = TOTAL_PAGES - pages_read

    # Display the number of pages Nate still needs to read
    result = pages_left
    return result

print(solution())