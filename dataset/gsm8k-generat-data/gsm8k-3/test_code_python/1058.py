def solution():
    """Tom reads 10 hours over 5 days.  He can read 50 pages per hour.  Assuming he reads the same amount every day how many pages does he read in 7 days?"""
    # Calculate the total number of pages Tom reads in 5 days
    total_pages = 10 * 50 * 5

    # Calculate how many pages Tom reads per day
    pages_per_day = total_pages / 5

    # Calculate how many pages Tom reads in 7 days
    pages_in_7_days = pages_per_day * 7

    # Display the number of pages Tom reads in 7 days
    result = pages_in_7_days
    return result

print(solution())