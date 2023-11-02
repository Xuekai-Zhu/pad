def solution():
    liza_speed = 20  # Liza reads 20 pages in an hour
    suzie_speed = 15  # Suzie reads 15 pages in an hour
    time = 3  # Liza and Suzie read for 3 hours

    # Calculate the total number of pages Liza reads in 3 hours
    liza_pages = liza_speed * time

    # Calculate the total number of pages Suzie reads in 3 hours
    suzie_pages = suzie_speed * time

    # Calculate the difference between the number of pages Liza and Suzie read in 3 hours
    page_difference = liza_pages - suzie_pages
    result = page_difference
    return result

print(solution())