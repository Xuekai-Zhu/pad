def solution():
    """Nate is reading a 400-page book. He finished reading 20% of the book. How many pages does he need to read to finish the book?"""
    # Define the total number of pages in the book
    total_pages = 400

    # Calculate the number of pages Nate has already read
    pages_read = total_pages * 0.2

    # Calculate the number of pages Nate still needs to read
    pages_to_read = total_pages - pages_read

    # return the result
    result = pages_to_read
    return result

print(solution())