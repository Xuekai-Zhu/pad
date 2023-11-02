def solution():
    """Arthur knows that he needs to finish 800 pages of reading over the summer. He has read 80% of a 500-page book and 1/5 of a 1000 page book. How many more pages does he need to reach to meet his goal?"""
    # Define the total pages Arthur needs to read
    total_pages = 800

    # Calculate the pages Arthur has already read
    pages_read = 0.8 * 500 + (1/5) * 1000

    # Calculate the pages Arthur still needs to read
    pages_left = total_pages - pages_read

    # Display the pages Arthur still needs to read
    result = pages_left
    return result

print(solution())