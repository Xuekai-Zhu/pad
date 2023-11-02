def solution():
    """There are 381 pages in Elliot’s book. He has already read 149 pages. If he reads 20 pages a day for a week, how many pages are still left to be read?"""
    
    # Define the total number of pages in the book
    total_pages = 381
    
    # Define the number of pages Elliot has already read
    read_pages = 149
    
    # Calculate the number of pages he will read in the next week
    weekly_read = 20 * 7
    
    # Calculate the total number of remaining pages
    remaining_pages = total_pages - read_pages - weekly_read
    
    # Return the result
    result = remaining_pages
    return result

print(solution())