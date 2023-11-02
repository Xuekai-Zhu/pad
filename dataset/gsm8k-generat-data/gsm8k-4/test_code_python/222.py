def solution():
    """Bekah had to read 408 pages for history class. She read 113 pages over the weekend and has 5 days left to finish her reading. How many pages will she need to read each day for 5 days to complete her assignment?"""
    # Define the total number of pages and the number of pages read so far
    total_pages = 408
    pages_read = 113

    # Calculate the number of pages left to read
    pages_left = total_pages - pages_read

    # Calculate the number of pages Bekah needs to read each day to finish in 5 days
    pages_per_day = pages_left / 5

    # return the result
    result = pages_per_day
    return result

print(solution())