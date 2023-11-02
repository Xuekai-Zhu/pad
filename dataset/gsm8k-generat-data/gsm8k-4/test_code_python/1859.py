def solution():
    """If Janet reads 80 pages a day and Belinda reads 30 pages a day, how many more pages does Janet read in 6 weeks?"""
    # Define the number of pages each person reads per day
    janet_pages_per_day = 80
    belinda_pages_per_day = 30

    # Calculate the total number of pages each person reads in 6 weeks
    janet_total_pages = janet_pages_per_day * 7 * 6
    belinda_total_pages = belinda_pages_per_day * 7 * 6

    # Calculate the difference in the number of pages each person reads
    page_difference = janet_total_pages - belinda_total_pages

    # Return the result
    result = page_difference
    return result

print(solution())