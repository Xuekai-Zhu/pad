def solution():
    """Dustin and Sam are both reading. Dustin can read 75 pages in an hour. Sam can read 24 pages in an hour. How many more pages does Dustin read in 40 minutes compared to Sam?"""
    # Define the number of pages Dustin can read per minute
    DUSTIN_RATE = 75 / 60
    
    # Define the number of pages Sam can read per minute
    SAM_RATE = 24 / 60

    # Calculate the number of pages Dustin can read in 40 minutes
    dustin_pages = DUSTIN_RATE * 40

    # Calculate the number of pages Sam can read in 40 minutes
    sam_pages = SAM_RATE * 40

    # Calculate the difference in the number of pages read
    difference = dustin_pages - sam_pages

    # Display the difference in the number of pages read
    result = difference
    return result

print(solution())