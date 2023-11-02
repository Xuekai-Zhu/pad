def solution():
    """Rene can finish reading 30 pages in 60 minutes. Lulu can read 27 pages in 60 minutes and Cherry can read 25 pages in 60 minutes. If they have been reading for 240 minutes now, how many pages have they finished reading in total?"""
    # Define the reading speeds for each person
    SPEED_RENE = 30/60  # pages per minute
    SPEED_LULU = 27/60  # pages per minute
    SPEED_CHERRY = 25/60  # pages per minute

    # Define the total time spent reading
    total_time = 240  # minutes

    # Calculate the total number of pages read by each person
    pages_rene = SPEED_RENE * total_time
    pages_lulu = SPEED_LULU * total_time
    pages_cherry = SPEED_CHERRY * total_time

    # Calculate the total number of pages read
    total_pages = pages_rene + pages_lulu + pages_cherry

    # Display the total number of pages read
    result = total_pages
    return result

print(solution())