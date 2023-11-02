def solution():
    # Calculate the number of pages Bill had read by the 12th of April
    pages_read = 8 * 12  # Bill read 8 pages every day for 12 days
    # Calculate the total number of pages in the book
    total_pages = (pages_read * 3) / 2  # Bill had covered two-thirds of the book by the 12th of April
    result = total_pages
    return result

print(solution())