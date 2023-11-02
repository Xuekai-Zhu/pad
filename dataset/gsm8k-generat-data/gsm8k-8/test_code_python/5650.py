def solution():
    # Calculate the number of pages Dustin can read in 40 minutes
    dustin_pages = (75 / 60) * 40

    # Calculate the number of pages Sam can read in 40 minutes
    sam_pages = (24 / 60) * 40

    # Calculate the difference in the number of pages they each read
    page_difference = dustin_pages - sam_pages

    result = page_difference
    return result

print(solution())