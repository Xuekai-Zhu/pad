def solution():
    """There are 381 pages in Elliot’s book.  He has already read 149 pages.  If he reads 20 pages a day for a week, how many pages are still left to be read?"""
    # Define the total number of pages in the book and the number of pages Elliot has already read
    TOTAL_PAGES = 381
    PAGES_READ = 149

    # Calculate the number of pages Elliot will read over the course of a week
    PAGES_READ_WEEK = 20 * 7

    # Calculate the total number of pages Elliot still needs to read
    pages_left = TOTAL_PAGES - PAGES_READ - PAGES_READ_WEEK

    # Display the total number of pages left to be read
    result = pages_left
    return result

print(solution())