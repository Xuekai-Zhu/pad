def solution():
    """Jerry has an interesting novel he borrowed from a friend to read over the weekend. The book has 93 pages. On Saturday, he reads 30 pages. On Sunday, he goes to church and comes back, sits down, and reads 20 pages of the book. How many pages are remaining before Jerry can finish the book?"""
    # Define the total number of pages in the book
    total_pages = 93

    # Calculate the number of pages Jerry has read
    pages_read = 30 + 20

    # Calculate the number of pages remaining
    pages_remaining = total_pages - pages_read

    # Return the result
    result = pages_remaining
    return result

print(solution())