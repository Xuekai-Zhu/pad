def solution():
    """Bill started reading a book on the first day of April. He read 8 pages every day and by the 12th of April, he had covered two-thirds of the book. How many pages does the book have?"""
    # Calculate the number of pages Bill read up to the 12th of April
    pages_read = 8 * 11

    # Calculate the total number of pages in the book
    total_pages = pages_read * 3 / 2

    # Display the total number of pages
    result = total_pages
    return result

print(solution())