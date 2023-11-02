def solution():
    # Calculate the number of pages Tom reads in 5 days
    pages_read = 10 * 50  # Tom reads 50 pages per hour for 10 hours over 5 days

    # Calculate the number of pages Tom reads in 7 days
    pages_in_7_days = pages_read * 7 / 5  # assuming he reads the same amount every day
    result = pages_in_7_days
    return result

print(solution())