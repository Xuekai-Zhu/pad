def solution():
    """Dustin can read 75 pages in an hour. Sam can read 24 pages in an hour. How many more pages does Dustin read in 40 minutes compared to Sam?"""
    # Calculate the number of pages Dustin can read in 40 minutes
    dustin_pages = (75/60) * 40

    # Calculate the number of pages Sam can read in 40 minutes
    sam_pages = (24/60) * 40

    # Calculate the difference in the number of pages they can read in 40 minutes
    page_difference = dustin_pages - sam_pages

    # return the result
    result = page_difference
    return result

print(solution())