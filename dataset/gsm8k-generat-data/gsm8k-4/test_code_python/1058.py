def solution():
    """Tom reads 10 hours over 5 days. He can read 50 pages per hour. Assuming he reads the same amount every day how many pages does he read in 7 days?"""
    # Calculate the total number of hours Tom reads each day
    daily_hours = 10 / 5

    # Calculate the total number of pages Tom reads each day
    daily_pages = daily_hours * 50

    # Calculate the total number of pages Tom reads in 7 days
    total_pages = daily_pages * 7

    # Return the result
    result = total_pages
    return result

print(solution())