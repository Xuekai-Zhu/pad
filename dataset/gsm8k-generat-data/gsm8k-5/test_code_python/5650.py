def solution():
    dustin_speed = 75 / 60  # Dustin can read 75 pages in an hour, so his speed is 75/60 pages per minute
    sam_speed = 24 / 60  # Sam can read 24 pages in an hour, so his speed is 24/60 pages per minute
    time = 40  # Dustin and Sam will read for 40 minutes

    # Calculate how many pages each person can read in the given time
    dustin_pages = dustin_speed * time
    sam_pages = sam_speed * time

    # Calculate the difference in the number of pages read
    page_difference = dustin_pages - sam_pages
    result = page_difference
    return result

print(solution())