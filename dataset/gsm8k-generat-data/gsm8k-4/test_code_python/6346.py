def solution():
    """Bill started reading a book on the first day of April. He read 8 pages every day and by the 12th of April, he had covered two-thirds of the book. How many pages does the book have?"""
    # Define the number of pages Bill reads each day
    daily_reading = 8

    # Define the fraction of the book Bill has covered
    fraction_covered = 2/3

    # Calculate the number of days Bill has been reading
    days_reading = 12

    # Calculate the total number of pages in the book
    total_pages = (days_reading * daily_reading) / fraction_covered

    # return the result
    result = int(total_pages)
    return result

print(solution())