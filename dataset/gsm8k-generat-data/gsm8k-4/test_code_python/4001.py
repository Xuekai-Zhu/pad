def solution():
    """Liza reads 20 pages in an hour, and Suzie reads 15 pages in an hour. How many more pages does Liza read than Suzie in 3 hours?"""
    # Define the reading speeds
    liza_speed = 20  # pages per hour
    suzie_speed = 15  # pages per hour

    # Calculate the number of pages each person can read in 3 hours
    liza_pages = liza_speed * 3
    suzie_pages = suzie_speed * 3

    # Calculate the difference in the number of pages read
    difference = liza_pages - suzie_pages

    # Return the result
    result = difference
    return result

print(solution())